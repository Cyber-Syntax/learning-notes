---
title: Backintime
tags:
  - backup
---

<!-- TOC -->

## Smart remove for backintime

> [!NOTE]
> smart remove:
> [source](https://bugs.launchpad.net/backintime/+bug/502435)

- keep one snapshot per month for all previous months of this year and all months of the last year
- This mean, it's gonna take 3 backup for 3 months, 4 backup for 4 weeks, 7 backup for 7 days.

## Exclude files

```ini
profile1.snapshots.exclude.1.value=target/
profile1.snapshots.exclude.2.value=SingletonLock
profile1.snapshots.exclude.3.value=SingletonCookie
profile1.snapshots.exclude.4.value=node_modules/
profile1.snapshots.exclude.5.value=lost+found/*
profile1.snapshots.exclude.6.value=lock
profile1.snapshots.exclude.7.value=Games/
profile1.snapshots.exclude.8.value=Applications/
profile1.snapshots.exclude.9.value=/var/tmp/*
profile1.snapshots.exclude.10.value=/var/cache/apt/archives/*.deb
profile1.snapshots.exclude.11.value=/var/backups/*
profile1.snapshots.exclude.12.value=/tmp/*
profile1.snapshots.exclude.13.value=/sys/*
profile1.snapshots.exclude.14.value=/swapfile
profile1.snapshots.exclude.15.value=/run/*
profile1.snapshots.exclude.16.value=/proc/*
profile1.snapshots.exclude.17.value=/home/developer/Downloads
profile1.snapshots.exclude.18.value=/home/developer/Documents/backup-for-cloud
profile1.snapshots.exclude.19.value=/etc/mtab
profile1.snapshots.exclude.20.value=/dev/*
profile1.snapshots.exclude.21.value=*node_modules
profile1.snapshots.exclude.22.value=*~
profile1.snapshots.exclude.23.value=*/.DS_Store
profile1.snapshots.exclude.24.value=*.venv*
profile1.snapshots.exclude.25.value=*.ruff_cache
profile1.snapshots.exclude.26.value=*.pyc
profile1.snapshots.exclude.27.value=*.backup*
profile1.snapshots.exclude.28.value=*.angular/cache
profile1.snapshots.exclude.29.value=.wine
profile1.snapshots.exclude.30.value=.var/app/com.spotify.Client/cache
profile1.snapshots.exclude.31.value=.var/app/**/[Cc]ache/
profile1.snapshots.exclude.32.value=.thumbnails*
profile1.snapshots.exclude.33.value=.stversions
profile1.snapshots.exclude.34.value=.pytest_cache
profile1.snapshots.exclude.35.value=.Private
profile1.snapshots.exclude.36.value=.npm/
profile1.snapshots.exclude.37.value=.mypy_cache
profile1.snapshots.exclude.38.value=.local/share/umu
profile1.snapshots.exclude.39.value=.local/share/Steam
profile1.snapshots.exclude.40.value=.local/share/lutris
profile1.snapshots.exclude.41.value=.local/share/containers/storage/overlay
profile1.snapshots.exclude.42.value=.local/share/[Tt]rash*
profile1.snapshots.exclude.43.value=.local/lib
profile1.snapshots.exclude.44.value=.gvfs
profile1.snapshots.exclude.45.value=.dropbox*
profile1.snapshots.exclude.46.value=.config/heroic
profile1.snapshots.exclude.47.value=.config_Backup
profile1.snapshots.exclude.48.value=.cargo/registry
profile1.snapshots.exclude.49.value=.cargo/cache
profile1.snapshots.exclude.50.value=.cache/*
profile1.snapshots.exclude.51.value=__pycache__/
profile1.snapshots.exclude.52.value=.mozilla/firefox/**/cache/
profile1.snapshots.exclude.53.value=.config/BraveSoftware/Brave-Browser/Default/Service Worker/CacheStorage/
# TESTING
profile1.snapshots.exclude.54.value=.config/Code/Cache/
profile1.snapshots.exclude.55.value=.config/Code/CachedData/
profile1.snapshots.exclude.56.value=.config/Code/CachedExtensionVSIXs/
profile1.snapshots.exclude.57.value=.config/Code/CachedExtensions/
profile1.snapshots.exclude.58.value=.config/Code/GPUCache/
profile1.snapshots.exclude.59.value=.config/Code/Service Worker/CacheStorage/
profile1.snapshots.exclude.60.value=.config/Code/Service Worker/ScriptCache/
profile1.snapshots.exclude.61.value=.config/Code/User/workspaceStorage/
profile1.snapshots.exclude.62.value=.vscode-server/extensionsCache/
profile1.snapshots.exclude.63.value=.vscode-server/data/CachedExtensions/
profile1.snapshots.exclude.64.value=.vscode-server/data/CachedProfilesData/
profile1.snapshots.exclude.65.value=.local/share/zed/
profile1.snapshots.exclude.66.value=.local/state/zed/
profile1.snapshots.exclude.67.value=.config/*/Cache/
profile1.snapshots.exclude.68.value=.config/*/GPUCache/
profile1.snapshots.exclude.69.value=.config/*/Code Cache/
profile1.snapshots.exclude.70.value=.config/*/Service Worker/CacheStorage/
profile1.snapshots.exclude.71.value=.config/*/Service Worker/ScriptCache/
profile1.snapshots.exclude.72.value=.pnpm-store/
profile1.snapshots.exclude.73.value=.yarn/cache/
profile1.snapshots.exclude.74.value=.yarn/unplugged/
profile1.snapshots.exclude.75.value=.parcel-cache/
profile1.snapshots.exclude.76.value=.turbo/
profile1.snapshots.exclude.77.value=.next/cache/
profile1.snapshots.exclude.78.value=.nuxt/
profile1.snapshots.exclude.79.value=.storybook-out/
profile1.snapshots.exclude.80.value=.vite/
profile1.snapshots.exclude.81.value=.esbuild/
profile1.snapshots.exclude.82.value=.ipynb_checkpoints/
profile1.snapshots.exclude.83.value=.jupyter/lab/staging/
profile1.snapshots.exclude.84.value=.jupyter/lab/workspaces/
profile1.snapshots.exclude.85.value=.cargo/git/
profile1.snapshots.exclude.86.value=.gradle/
profile1.snapshots.exclude.87.value=.m2/repository/
profile1.snapshots.exclude.88.value=.local/share/docker/
profile1.snapshots.exclude.89.value=.local/share/containers/cache/
profile1.snapshots.exclude.90.value=.local/share/containers/storage/overlay-images/
profile1.snapshots.exclude.91.value=dist/
profile1.snapshots.exclude.92.value=build/
profile1.snapshots.exclude.93.value=out/
profile1.snapshots.exclude.94.value=coverage/
profile1.snapshots.exclude.95.value=logs/
profile1.snapshots.exclude.96.value=*.log
profile1.snapshots.exclude.97.value=*.tmp
profile1.snapshots.exclude.98.value=*.cache
profile1.snapshots.exclude.99.value=.config/*/Cache/
profile1.snapshots.exclude.100.value=.config/*/Code Cache/
profile1.snapshots.exclude.101.value=.config/*/GPUCache/
profile1.snapshots.exclude.102.value=.config/*/DawnGraphiteCache/
profile1.snapshots.exclude.103.value=.config/*/DawnWebGPUCache/
profile1.snapshots.exclude.104.value=.config/*/IndexedDB/
profile1.snapshots.exclude.105.value=.config/*/blob_storage/
profile1.snapshots.exclude.106.value=.config/*/Session Storage/
profile1.snapshots.exclude.107.value=.config/*/Local Storage/
profile1.snapshots.exclude.108.value=.config/*/shared_proto_db/
profile1.snapshots.exclude.109.value=.config/*/Dictionaries/
profile1.snapshots.exclude.110.value=.config/*/Service Worker/CacheStorage/
profile1.snapshots.exclude.111.value=.config/*/Service Worker/ScriptCache/
profile1.snapshots.exclude.112.value=.config/*/Crashpad/
profile1.snapshots.exclude.113.value=.config/*/*.log
profile1.snapshots.exclude.114.value=.var/app/*/cache/
profile1.snapshots.exclude.115.value=.var/app/*/config/*/Cache/
profile1.snapshots.exclude.116.value=.var/app/*/config/*/GPUCache/
profile1.snapshots.exclude.117.value=.var/app/*/config/*/Code Cache/
profile1.snapshots.exclude.118.value=.local/share/*/Cache/
profile1.snapshots.exclude.119.value=.local/share/*/GPUCache/
profile1.snapshots.exclude.120.value=.local/share/*/Code Cache/
profile1.snapshots.exclude.121.value=.config/BraveSoftware/Brave-Browser/ShaderCache/
profile1.snapshots.exclude.122.value=.config/BraveSoftware/Brave-Browser/GrShaderCache/
profile1.snapshots.exclude.123.value=.config/BraveSoftware/Brave-Browser/GraphiteDawnCache/
profile1.snapshots.exclude.124.value=.config/BraveSoftware/Brave-Browser/component_crx_cache/
profile1.snapshots.exclude.125.value=.config/BraveSoftware/Brave-Browser/extensions_crx_cache/
profile1.snapshots.exclude.126.value=.config/BraveSoftware/Brave-Browser/Guest Profile/GPUCache/
profile1.snapshots.exclude.127.value=.config/BraveSoftware/Brave-Browser/Default/GPUCache/
profile1.snapshots.exclude.128.value=.config/BraveSoftware/Brave-Browser/Default/DawnCache/
profile1.snapshots.exclude.129.value=.config/BraveSoftware/Brave-Browser/Default/optimization_guide_hint_cache_store/
profile1.snapshots.exclude.130.value=.config/BraveSoftware/Brave-Browser/Default/Shared Dictionary/cache/
profile1.snapshots.exclude.131.value=.config/BraveSoftware/Brave-Browser/Default/Service Worker/ScriptCache/
```

## Storage

#### How to copy the backup files without losing hard links(incremental)

> [!NOTE]
>
> If you don't use the H you end up creating new folder for each hard link which it would make 25G backup 125G

### 1) Copy the existing backup directory to the new partition (preserving hard-links)

Back In Time stores each snapshot with lots of hard links between unchanged files. A normal file copy would break these links and make all backups huge — but rsync can preserve them:

```bash
rsync -avhH --progress /mnt/sda2/backintime /mnt/backups/
```

`-a` archive mode (preserves permissions, timestamps)
`-h` human-readable
`-H` **important**: preserves **hard links** so your incrementals stay incrementals
`--progress` just shows progress ([Hammer’s Blog][2])

#### 2) **Update Back In Time’s config with the new path**

Once the backup data is on the new partition, Back In Time still has the _old_ location in its config. You need to edit this manually:

1. Open your config file, usually at:

   ```
   ~/.config/backintime/config
   ```

2. Find the line (for your profile):

   ```
   profile1.snapshots.path=/old/backup/path
   ```

3. Change it to your new mount point:

   ```
   profile1.snapshots.path=/new/backup/path
   ```

4. Save and close.

💡 Now Back In Time will point to the new location and see your existing snapshot history. ([Ask Ubuntu][3])

---

#### 3) **Verify & Run a Backup**

After making the config change:

- Start Back In Time → you should see your old snapshots listed.
- Run a backup — the next snapshot should hard-link unchanged files to the old ones, just like before.

If it shows a _full_ backup copying everything again, it usually means:

- Hard links weren’t preserved in the move, **or**
- The path in the config still doesn’t match the actual backup hierarchy.

---

## ⚠️ Things to Watch

- The **new partition must be on a filesystem that supports hard-links** (e.g., ext4, XFS, Btrfs). NTFS, FAT32, some network filesystems don’t — Back In Time won’t share unchanged files properly. ([backintime.readthedocs.io][4])
- Make sure the partition is **mounted before Back In Time runs** — if it can’t find the path, it will fail.

[1]: https://askubuntu.com/questions/796061/how-to-move-entire-back-in-time-backup-set-to-new-hard-drive?utm_source=chatgpt.com "How to move entire Back In Time backup set to new hard ..."
[2]: https://blog.monotok.org/posts/linux-move-back-time-backups/?utm_source=chatgpt.com "Linux - Move back in time backups - Hammer's Blog"
[3]: https://askubuntu.com/questions/183743/cant-reset-backintime-snapshot-path?utm_source=chatgpt.com "Can't reset BackInTime snapshot path"
[4]: https://backintime.readthedocs.io/en/latest/manage-profiles.html?utm_source=chatgpt.com "Manage profiles - Back In Time - User Manual"

<!-- /TOC -->
