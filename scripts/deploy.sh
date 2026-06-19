#!/usr/bin/env bash

set -euo pipefail

BUILD_DIR="site"
TEMP_DIR="/tmp/mkdocs-gh-pages"
ORIG_BRANCH=""
DEPLOY_BRANCH="gh-pages"
SOURCE_BRANCH="main"

log() {
  local msg
  msg="$1"
  printf "%s\n" "$msg"
}

error() {
  local msg
  msg="$1"
  printf "ERROR: %s\n" "$msg" >&2
}

cleanup() {
  if [[ -n "${ORIG_BRANCH}" ]]; then
    git checkout "${ORIG_BRANCH}" >/dev/null 2>&1 || true
  fi
}

trap cleanup EXIT INT TERM

validate_env() {
  if ! command -v git >/dev/null 2>&1; then
    error "git is not installed"
    return 1
  fi

  if [[ ! -d .git ]]; then
    error "not a git repository"
    return 1
  fi
}

get_current_branch() {
  local branch
  if ! branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null); then
    error "failed to determine current git branch"
    return 1
  fi

  if [[ -z "${branch// /}" ]]; then
    error "empty git branch name detected"
    return 1
  fi

  ORIG_BRANCH="${branch}"
}

build_docs() {
  if ! uv run mkdocs build --clean; then
    error "mkdocs build failed"
    return 1
  fi

  if [[ ! -d "${BUILD_DIR}" ]]; then
    error "build directory missing: ${BUILD_DIR}"
    return 1
  fi
}

prepare_temp() {
  rm -rf "${TEMP_DIR}"

  if ! mkdir -p "${TEMP_DIR}"; then
    error "failed to create temp directory"
    return 1
  fi

  if ! cp -r "${BUILD_DIR}/"* "${TEMP_DIR}/" 2>/dev/null; then
    error "failed to copy build artifacts"
    return 1
  fi
}

switch_branch() {
  git fetch origin || true

  if git show-ref --verify --quiet "refs/heads/${DEPLOY_BRANCH}"; then
    if ! git checkout "${DEPLOY_BRANCH}"; then
      error "failed to checkout ${DEPLOY_BRANCH}"
      return 1
    fi
  else
    if ! git checkout --orphan "${DEPLOY_BRANCH}"; then
      error "failed to create orphan branch ${DEPLOY_BRANCH}"
      return 1
    fi
  fi
}

deploy_content() {
  rm -rf ./*

  if ! cp -r "${TEMP_DIR}/"* . 2>/dev/null; then
    error "failed to copy temp content to repo root"
    return 1
  fi

  git add -A || true

  if git diff --cached --quiet; then
    log "No changes to deploy"
    return 0
  fi

  local ts
  ts=$(date -u '+%Y-%m-%d %H:%M:%S UTC')

  if [[ -z "${ts// /}" ]]; then
    error "failed to generate timestamp"
    return 1
  fi

  if ! git commit -m "deploy: ${ts}"; then
    error "git commit failed"
    return 1
  fi

  if ! git push origin "${DEPLOY_BRANCH}"; then
    error "git push failed"
    return 1
  fi
}

restore_branch() {
  if [[ -n "${ORIG_BRANCH}" ]]; then
    git checkout "${ORIG_BRANCH}" >/dev/null 2>&1 || {
      error "failed to restore original branch"
      return 1
    }
  fi
}

main() {
  validate_env || return 1
  get_current_branch || return 1

  build_docs || return 1
  prepare_temp || return 1

  switch_branch || return 1
  deploy_content || return 1

  restore_branch || return 1

  log "deployment completed successfully"
}

main "$@"

