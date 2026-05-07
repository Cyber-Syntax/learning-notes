"""
A more realistic multi-package package-manager example.

This demonstrates:

1. stdout vs stderr
2. logging to file
3. progress bars
4. warnings
5. expected exceptions
6. unexpected exceptions
7. transaction summaries
8. batch installs
9. continuing after failures
10. clean CLI architecture

IMPORTANT CLI DESIGN PRINCIPLE
==============================

stdout:
    Actual command result / machine-readable data

stderr:
    Progress bars, warnings, install commentary, errors

logs:
    Internal diagnostics for developers/operators

These are THREE separate concerns.
"""

from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

# -----------------------------------------------------------------------------
# LOGGING
# -----------------------------------------------------------------------------
#
# Logs go to file.
#
# User-facing terminal UI is separate.
# -----------------------------------------------------------------------------

logging.basicConfig(
    filename="myapp.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)


# -----------------------------------------------------------------------------
# TERMINAL HELPERS
# -----------------------------------------------------------------------------
#
# emit()
# -------
# stderr terminal UI
#
# output()
# --------
# stdout machine-readable output
# -----------------------------------------------------------------------------


def emit(message: str) -> None:
    print(message, file=sys.stderr)


def output(message: str) -> None:
    print(message)


# -----------------------------------------------------------------------------
# EXCEPTIONS
# -----------------------------------------------------------------------------


class PackageNotFoundError(Exception):
    pass


class AssetNotFoundError(Exception):
    pass


class DownloadError(Exception):
    pass


class InstallError(Exception):
    pass


# -----------------------------------------------------------------------------
# MOCK PACKAGE DATABASE
# -----------------------------------------------------------------------------
#
# This simulates package/API states.
#
# Real applications would fetch this from GitHub APIs.
# -----------------------------------------------------------------------------

PACKAGE_DATABASE = {
    "qownnotes": {
        "version": "26.2.4",
        "size_mb": 41.6,
    },
    "appflowy": {
        "version": "0.11.1",
        "size_mb": 77.6,
    },
    "weektodo": {
        "version": "1.30.1",
        "size_mb": 139.5,
        "checksum_missing": True,
    },
    "ytmdesktop": {
        "asset_missing": True,
    },
    "obsidian": {
        "version": "1.8.10",
        "size_mb": 92.1,
    },
    "notion": {
        "version": "3.1.0",
        "size_mb": 80.2,
        "install_fail": True,
    },
}


# -----------------------------------------------------------------------------
# FETCH METADATA
# -----------------------------------------------------------------------------
#
# We DO NOT print low-level technical details to users.
#
# User gets simple commentary.
#
# Developers get detailed logs.
# -----------------------------------------------------------------------------


def fetch_metadata(package_name: str) -> dict:
    logger.info(
        "Fetching metadata package=%s",
        package_name,
    )

    time.sleep(0.3)

    package = PACKAGE_DATABASE.get(package_name)

    if package is None:
        logger.error(
            "Package not found package=%s",
            package_name,
        )

        raise PackageNotFoundError(package_name)

    if package.get("asset_missing"):
        logger.error(
            "AppImage asset missing package=%s",
            package_name,
        )

        raise AssetNotFoundError(package_name)

    logger.info(
        "Metadata fetched package=%s version=%s",
        package_name,
        package["version"],
    )

    return package


# -----------------------------------------------------------------------------
# DOWNLOAD
# -----------------------------------------------------------------------------
#
# Progress bars belong to stderr.
#
# WHY?
#
# Because they are terminal UI.
#
# They are NOT actual command results.
# -----------------------------------------------------------------------------


def download_package(package_name: str, size_mb: float) -> Path:
    logger.info(
        "Download started package=%s size_mb=%.1f",
        package_name,
        size_mb,
    )

    total_steps = 20

    for step in range(total_steps + 1):
        percent = int((step / total_steps) * 100)

        filled = "#" * step
        empty = "." * (total_steps - step)

        print(
            f"\r{package_name:<12} "
            f"{size_mb:>6.1f} MiB   "
            f"[{filled}{empty}] "
            f"{percent:>3}%",
            end="",
            file=sys.stderr,
            flush=True,
        )

        time.sleep(0.03)

    print(file=sys.stderr)

    logger.info(
        "Download completed package=%s",
        package_name,
    )

    return Path(f"/tmp/{package_name}.AppImage")


# -----------------------------------------------------------------------------
# CHECKSUM
# -----------------------------------------------------------------------------


def verify_checksum(package_name: str, metadata: dict) -> None:
    logger.info(
        "Verifying checksum package=%s",
        package_name,
    )

    if metadata.get("checksum_missing"):
        emit(f"warning: checksum asset not found for {package_name}")

        logger.warning(
            "Checksum asset missing package=%s",
            package_name,
        )

        return

    logger.info(
        "Checksum verified package=%s",
        package_name,
    )


# -----------------------------------------------------------------------------
# INSTALL
# -----------------------------------------------------------------------------


def install_package(package_name: str, path: Path, metadata: dict) -> None:
    logger.info(
        "Installing package=%s path=%s",
        package_name,
        path,
    )

    time.sleep(0.5)

    if metadata.get("install_fail"):
        logger.error(
            "Installation failed package=%s",
            package_name,
        )

        raise InstallError(package_name)

    logger.info(
        "Installation completed package=%s",
        package_name,
    )


# -----------------------------------------------------------------------------
# MAIN TRANSACTION
# -----------------------------------------------------------------------------
#
# IMPORTANT DESIGN:
#
# We process ALL packages even if some fail.
#
# Package managers usually continue transaction work.
#
# We collect:
#
#   - installed
#   - failed
#   - warnings
#
# instead of crashing immediately.
# -----------------------------------------------------------------------------


def install_packages(package_names: list[str]) -> int:
    logger.info(
        "Transaction started package_count=%s",
        len(package_names),
    )

    installed = []
    failed = []

    # -------------------------------------------------------------------------
    # RESOLVING
    # -------------------------------------------------------------------------

    emit(":: Resolving packages...")

    metadata_map = {}

    for package_name in package_names:
        try:
            metadata_map[package_name] = fetch_metadata(package_name)

        except PackageNotFoundError:
            emit(f"error: package not found: {package_name}")

            failed.append(package_name)

        except AssetNotFoundError:
            emit(f"error: AppImage asset not found: {package_name}")

            failed.append(package_name)

    # -------------------------------------------------------------------------
    # DOWNLOADS
    #
    # Only ONE section heading.
    #
    # This is how real package managers behave.
    # -------------------------------------------------------------------------

    emit(":: Downloading packages...")

    downloaded_paths = {}

    for package_name, metadata in metadata_map.items():
        if package_name in failed:
            continue

        try:
            downloaded_paths[package_name] = download_package(
                package_name,
                metadata["size_mb"],
            )

        except DownloadError:
            emit(f"error: failed downloading {package_name}")

            logger.exception(
                "Download failure package=%s",
                package_name,
            )

            failed.append(package_name)

    # -------------------------------------------------------------------------
    # CHECKSUMS
    # -------------------------------------------------------------------------

    emit(":: Verifying checksums...")

    for package_name, metadata in metadata_map.items():
        if package_name in failed:
            continue

        verify_checksum(package_name, metadata)

    # -------------------------------------------------------------------------
    # INSTALLATION
    #
    # Again:
    #
    # ONE transaction section heading.
    # -------------------------------------------------------------------------

    emit(":: Installing packages...")

    for package_name, path in downloaded_paths.items():
        if package_name in failed:
            continue

        emit(f"installing {package_name}...")

        try:
            install_package(
                package_name,
                path,
                metadata_map[package_name],
            )

            installed.append(
                (
                    package_name,
                    metadata_map[package_name]["version"],
                )
            )

        except InstallError:
            emit(f"error: installation failed: {package_name}")

            logger.exception(
                "Install failure package=%s",
                package_name,
            )

            failed.append(package_name)

        except Exception:
            # -----------------------------------------------------------------
            # Unexpected crash.
            #
            # logger.exception logs FULL traceback.
            # -----------------------------------------------------------------

            emit(f"error: unexpected install failure: {package_name}")

            logger.exception(
                "Unexpected install failure package=%s",
                package_name,
            )

            failed.append(package_name)

    # -------------------------------------------------------------------------
    # TRANSACTION SUMMARY
    # -------------------------------------------------------------------------

    emit(":: Transaction summary")

    for package_name, version in installed:
        emit(f"INSTALLED  {package_name:<12} {version}")

    for package_name in failed:
        emit(f"FAILED     {package_name}")

    # -------------------------------------------------------------------------
    # MACHINE-READABLE OUTPUT
    #
    # This is the REAL command result.
    #
    # This belongs to stdout.
    #
    # Another program could safely parse this.
    # -------------------------------------------------------------------------

    output(
        str(
            {
                "installed": [name for name, _ in installed],
                "failed": failed,
            }
        )
    )

    logger.info(
        "Transaction finished installed=%s failed=%s",
        len(installed),
        len(failed),
    )

    # non-zero if ANY package failed
    return 1 if failed else 0


# -----------------------------------------------------------------------------
# ENTRYPOINT
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    raise SystemExit(
        install_packages(
            [
                "qownnotes",
                "appflowy",
                "weektodo",
                "ytmdesktop",
                "obsidian",
                "notion",
            ]
        )
    )
