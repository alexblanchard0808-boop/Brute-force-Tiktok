#!/bin/bash
set -euo pipefail

# Check if running as root
if [ "$(id -u)" -eq 0 ]; then
    python3 Brute-force-tiktok.py
else
    sudo python3 Brute-force-tiktok.py
fi
