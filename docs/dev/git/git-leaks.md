---
title: How to scan leaks on your repositories?
id: git-leaks
last_update:
  date: 06/06/2025
publish_date:
  date: 23/06/2025
tags:
  - git
---

<!-- TOC -->

## Scan secrets via gitleaks

```bash
gitleaks dir ~/Documents/repository --report-path gitleaks-report.json

gitleaks dir ~/dotfiles --report-path gitleaks-dotfiles.json
```

<!-- /TOC -->
