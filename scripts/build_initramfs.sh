#!/bin/bash

set -e

ROOTFS_DIR="../alpine-rootfs"
INITRAMFS="../initramfs.gz"

echo "Installing Python inference packages..."
cd "$ROOTFS_DIR"
./usr/bin/python3 -m pip install --root . --no-cache-dir onnxruntime tflite-runtime transformers sentence-transformers

echo "Stripping unnecessary packages..."
# Remove development packages, docs, etc.
./sbin/apk del --purge apk-tools || true
./sbin/apk del --purge python3-dev || true
# Add more if needed

echo "Cleaning up..."
rm -rf var/cache/apk/*
rm -rf usr/share/doc/*
rm -rf usr/share/man/*

echo "Creating initramfs..."
find . -print0 | cpio -0 -H newc -o | gzip -9 > "$INITRAMFS"

echo "Initramfs created at $INITRAMFS"
du -h "$INITRAMFS"