# AetherDrive

An AI-powered bootable USB utility with a personality.
Yeah, I know. Stupid right? It can also run Doom.
Who's stupid now?
## Overview

AetherDrive uses advanced AI models to automatically detect and configure boot entries for ISOs placed on the USB drive. It supports Windows, Linux, macOS, and more, with features like persistence, theme selection, and smart healing.

## Architecture

- **Bootloader**: systemd-boot, rEFInd, GRUB fallback

- **NPU**: ONNX/TFLite models for OS detection and boot configuration

- **Scripts**: Automation scripts (magic spells)

- **Tools**: Binaries like xorriso, wimlib, etc.

- **Persist**: Persistent data (SQLite, JSON)

- **THEMES**: rEFInd themes gruuvbox polarized south moch dotfile manburger

## Partition Layout

The USB drive is partitioned into three partitions based on Ventoy's scheme with additions:
Partition order: ESP (1), Data (2), AETHER (3)

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



This layout ensures compatibility with UEFI firmware and allows the AI to run in RAM without modifying the data partition.



-- -- --- -- - -- --- -- - --%BuildInosense% bowalkadesigns 2025 -- - --- -- - -- -- -- -
