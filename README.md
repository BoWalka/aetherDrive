# AetherDrive

An AI-powered bootable USB utility that requires zero user knowledge to boot any OS.

## Overview

AetherDrive uses advanced AI models to automatically detect and configure boot entries for ISOs placed on the USB drive. It supports Windows, Linux, macOS, and more, with features like persistence, theme selection, and smart healing.

## Architecture

- **Bootloader**: systemd-boot, rEFInd, GRUB fallback

- **AI Brain**: ONNX/TFLite models for OS detection and boot configuration

- **Scripts**: Automation scripts

- **Tools**: Binaries like xorriso, wimlib, etc.

- **Persist**: Persistent data (SQLite, JSON)

- **Themes**: rEFInd themes

## Partition Layout

The USB drive is partitioned into three partitions based on Ventoy's scheme with additions:

1. **EFI System Partition (ESP)**:
   - Size: 100 MB
   - Filesystem: FAT32
   - Label: EFI
   - Purpose: Stores bootloaders (systemd-boot, rEFInd, GRUB), EFI binaries, and boot configurations.

2. **Data Partition**:
   - Size: Remaining space after ESP and AETHER
   - Filesystem: exFAT
   - Label: VTOYEFI (following Ventoy convention)
   - Purpose: Stores user ISOs, images, and other bootable files.

3. **AETHER Partition**:
   - Size: 128 MB
   - Filesystem: FAT32
   - Label: AETHER
   - Purpose: Contains AI models (ONNX/TFLite), configuration files, persistent data (SQLite/JSON), cache, and the initramfs for the AI orchestrator.

Partition order: ESP (1), Data (2), AETHER (3)

This layout ensures compatibility with UEFI firmware and allows the AI to run in RAM without modifying the data partition.

## GitHub Repository Setup

To set up the GitHub repository:

1. Go to [GitHub.com](https://github.com) and sign in.
2. Click "New repository".
3. Name it `AetherDrive`.
4. Make it public.
5. Check "Add a README file" (but since we have one, or not).
6. Check "Add .gitignore" if needed.
7. Click "Create repository".
8. In the repository, go to Settings > Pages or wait, for LFS, it's enabled by default now? Wait, GitHub has LFS enabled for all repos.
GitHub has Git LFS enabled for all repositories since 2018 or so.
So, no need to enable separately.
The local repo is set up with LFS.
To push to GitHub, the user can do `git remote add origin https://github.com/username/AetherDrive.git && git push -u origin main`

## Build Instructions

[Will be added later]

## License

MIT License