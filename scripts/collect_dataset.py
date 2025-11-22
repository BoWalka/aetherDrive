#!/usr/bin/env python3

import os
import re
import json
import requests
from pathlib import Path

DATASET_DIR = Path("../dataset")
LABELS_FILE = DATASET_DIR / "labels.json"

# List of ISO URLs (sample, expand to 100k+)
ISO_URLS = [
    "https://releases.ubuntu.com/22.04/ubuntu-22.04.3-desktop-amd64.iso",
    "https://download.fedoraproject.org/pub/fedora/linux/releases/38/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-38-1.6.iso",
    "https://www.debian.org/CD/live/current/amd64/iso-hybrid/debian-live-12.1.0-amd64-standard.iso",
    # Add more URLs here
]

def download_file(url, dest):
    response = requests.get(url, stream=True)
    with open(dest, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def extract_labels(filename):
    labels = {}
    name = filename.lower()

    # OS name
    if 'ubuntu' in name:
        labels['os_name'] = 'Ubuntu'
    elif 'fedora' in name:
        labels['os_name'] = 'Fedora'
    elif 'debian' in name:
        labels['os_name'] = 'Debian'
    elif 'windows' in name:
        labels['os_name'] = 'Windows'
    elif 'kali' in name:
        labels['os_name'] = 'Kali'
    else:
        labels['os_name'] = 'Unknown'

    # Version
    version_match = re.search(r'(\d+\.\d+[\.\d]*)', name)
    labels['version'] = version_match.group(1) if version_match else 'Unknown'

    # Architecture
    if 'amd64' in name or 'x86_64' in name:
        labels['architecture'] = 'x86_64'
    elif 'i386' in name or 'i686' in name:
        labels['architecture'] = 'i386'
    else:
        labels['architecture'] = 'Unknown'

    # Bootloader
    if labels['os_name'] == 'Ubuntu':
        labels['bootloader'] = 'GRUB'
    elif labels['os_name'] == 'Windows':
        labels['bootloader'] = 'bootmgr'
    else:
        labels['bootloader'] = 'GRUB'

    # Kernel params (sample)
    labels['kernel_params'] = 'quiet splash' if labels['os_name'] == 'Ubuntu' else ''

    # Persistence compatible
    labels['ventoy_compatible'] = True

    # Filesystem
    labels['filesystem'] = 'ext4' if 'linux' in name else 'ntfs'

    return labels

def main():
    DATASET_DIR.mkdir(exist_ok=True)
    labels = {}

    for url in ISO_URLS:
        filename = url.split('/')[-1]
        dest = DATASET_DIR / filename

        if not dest.exists():
            print(f"Downloading {filename}...")
            download_file(url, dest)

        labels[filename] = extract_labels(filename)

    with open(LABELS_FILE, 'w') as f:
        json.dump(labels, f, indent=2)

    print(f"Dataset collected. Labels saved to {LABELS_FILE}")

if __name__ == "__main__":
    main()