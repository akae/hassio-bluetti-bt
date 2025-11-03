# hassio-bluetti-bt
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)
[![Validate with hassfest](https://github.com/Patrick762/hassio-bluetti-bt/actions/workflows/hassfest_validation.yml/badge.svg)](https://github.com/Patrick762/hassio-bluetti-bt/actions/workflows/hassfest_validation.yml)
[![HACS Action](https://github.com/Patrick762/hassio-bluetti-bt/actions/workflows/HACS.yml/badge.svg)](https://github.com/Patrick762/hassio-bluetti-bt/actions/workflows/HACS.yml)

Bluetti Integration for Home Assistant - **Now with Encryption Support**

## Disclaimer
This integration is provided without any warranty or support by Bluetti (unfortunately). I do not take responsibility for any problems it may cause in all cases. Use it at your own risk.

## Features

- ✅ **Backward Compatible**: Works with all existing non-encrypted Bluetti devices
- 🔐 **Encryption Support**: Optional support for newer encrypted Bluetti devices
- 🔄 **Auto-Detection**: Automatically detects if encryption is needed
- 📊 **Full Data Access**: Read sensors, control outputs, and monitor device status

## Installation

### Method 1: Using HACS (Recommended)

To install this integration, you first need [HACS](https://hacs.xyz/) installed.
After the installation, you can use this button to install the integration:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Patrick762&repository=hassio-bluetti-bt&category=integration)

### Supported devices:

- AC60
- AC70 (basic data)
- AC70P (untested)
- AC180 (basic data)
- AC180P (tested)
- AC200L (untested)
- AC200M
- AC300 (tested)
- AC500 (tested)
- EB3A (tested, encryption enabled working)
- EP500
- EP500P
- EP600 (tested)
- EP760 (basic data)
- EP800 (basic data)

### Available controls:
If enabled in the Integration options (you need to reload the integration if you change this option):
AC and DC outputs

## Encryption Setup (For newer encrypted devices)

Some newer Bluetti devices require encrypted communication. If your device needs encryption support:

1. **Download the encryption module** from [Bluetti's official releases](https://github.com/bluetti-official/bluetti-bluetooth-lib/releases/)
2. **Extract** `bluetti_crypt.py` and `_bluetti_crypt.so` (or `.pyd` for Windows)
3. **Copy files** to your Python site-packages directory:
   ```bash
   # For Home Assistant OS (in container):
   docker exec -it homeassistant bash
   cp bluetti_crypt.py _bluetti_crypt.so /usr/local/lib/python3.*/site-packages/
   ```
4. **Get authorization file** `bluetti_device_licence.csv` from Bluetti (requires Communication Board SN from your device)
5. **Place authorization file** in `/config/` directory
6. **Restart Home Assistant** completely

**Note**: Integration works without encryption for older devices. Encryption is only needed for newer models that require it.

