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

1. Add this repository as a custom repository in HACS:
   - Go to HACS → Integrations → ⋮ (three dots) → Custom repositories
   - Add repository URL: `https://github.com/akae/hassio-bluetti-bt`
   - Category: Integration
   - Click "ADD"

2. Install the integration:
   - Search for "Bluetti BT" in HACS
   - Click "Download"
   - Restart Home Assistant

### Method 2: Manual Installation

1. Copy the `custom_components/bluetti_bt` folder to your Home Assistant `custom_components` directory
2. Restart Home Assistant

## Basic Setup (Works with all devices)

1. Go to Settings → Devices & Services → Add Integration
2. Search for "Bluetti BT" and select it
3. Follow the setup wizard to pair your device
4. The integration will work immediately with non-encrypted devices

## Encryption Setup (For newer encrypted devices)

Some newer Bluetti devices require encrypted communication. If your device needs encryption, follow these additional steps:

### Step 1: Download Bluetti Encryption Module

1. **Download the official encryption module** from Bluetti:
   - Go to: [https://github.com/bluetti-official/bluetti-bluetooth-lib/releases/](https://github.com/bluetti-official/bluetti-bluetooth-lib/releases/)
   - Download the latest `bluetti_crypt.zip` file

2. **Extract the files**:
   ```bash
   unzip bluetti_crypt.zip
   ```
   You should get:
   - `bluetti_crypt.py` - Python package
   - `_bluetti_crypt.so` (Linux/macOS) or `_bluetti_crypt.pyd` (Windows) - Binary library

### Step 2: Install Encryption Module in Home Assistant

#### For Home Assistant OS (Recommended):

1. **Access the Home Assistant container**:
   ```bash
   docker exec -it homeassistant bash
   ```

2. **Find your Python site-packages directory**:
   ```bash
   python3 -c "import site; print(site.getsitepackages())"
   ```

3. **Copy the encryption files**:
   ```bash
   # Copy to the site-packages directory (adjust path as needed)
   cp bluetti_crypt.py /usr/local/lib/python3.11/site-packages/
   cp _bluetti_crypt.so /usr/local/lib/python3.11/site-packages/
   ```

#### For Home Assistant Core/Container:

1. **Copy files to your Python installation**:
   ```bash
   # Example for typical Linux installation
   sudo cp bluetti_crypt.py _bluetti_crypt.so /usr/local/lib/python3.11/site-packages/
   ```

2. **Set proper permissions**:
   ```bash
   sudo chmod 644 /usr/local/lib/python3.11/site-packages/bluetti_crypt.py
   sudo chmod 755 /usr/local/lib/python3.11/site-packages/_bluetti_crypt.so
   ```

### Step 3: Get Device Authorization

1. **Find your Communication Board SN**:
   - Open the official Bluetti mobile app
   - Go to Settings → About Device
   - Note down the "Communication Board SN"

2. **Request authorization file**:
   - Contact Bluetti support with your Communication Board SN
   - Request the `bluetti_device_licence.csv` file
   - Or check if it's included in the encryption module download

3. **Install the authorization file**:
   ```bash
   # Copy to Home Assistant config directory
   cp bluetti_device_licence.csv /config/
   ```

### Step 4: Restart and Test

1. **Restart Home Assistant** completely
2. **Re-add your Bluetti device** through the integration
3. **Check the logs** for encryption status:
   ```
   Settings → System → Logs
   Search for "bluetti" or "crypt"
   ```

## Encryption Status Check

You can verify if encryption is working by checking the Home Assistant logs:

- ✅ **Encryption Working**: Look for `"Encryption support detected for device [DeviceName]"`
- ⚠️ **No Encryption Module**: `"bluetti_crypt module not available - encryption features disabled"`
- ℹ️ **Non-encrypted Device**: `"No metadata available for device [DeviceName], assuming non-encrypted"`

## Troubleshooting Encryption

### Common Issues:

1. **"Module not found" errors**:
   - Ensure files are in the correct Python path
   - Check file permissions
   - Restart Home Assistant completely

2. **"Authorization failed" errors**:
   - Verify the `bluetti_device_licence.csv` file is correct
   - Ensure the Communication Board SN matches
   - Check file location and permissions

3. **"Device not responding" after encryption setup**:
   - Try removing and re-adding the integration
   - Check Bluetooth connectivity
   - Verify device is in pairing mode

### Getting Help:

- Check the [Issues](https://github.com/akae/hassio-bluetti-bt/issues) page
- Include logs when reporting problems
- Mention your device model and Home Assistant setup type

### Supported devices:

**✅ Tested & Working:**
- AC180P (tested)
- AC200M (tested)
- AC300 (tested) 
- AC500 (tested)
- EB3A (tested, encryption working)
- EP600 (tested)

**⚠️ Basic Support:**
- AC60 (basic data)
- AC70 (basic data)
- AC70P (untested)
- AC180 (basic data)
- AC200L (untested)
- EP500 (basic data)
- EP500P (basic data)
- EP760 (basic data)
- EP800 (basic data)

**🔐 Encryption Support:**
- EB3A: ✅ Confirmed working
- Newer AC/EP models: Likely supported (requires testing)
- Older models: Use non-encrypted communication

### Available controls:

If enabled in the Integration options (you need to reload the integration if you change this option):
- **AC Output Control**: Turn AC outlets on/off
- **DC Output Control**: Turn DC outlets on/off  
- **Device Monitoring**: Battery level, power consumption, charging status
- **Real-time Data**: Voltage, current, temperature readings

## Version History

### v0.1.6 - Encryption Support
- ✨ Added Bluetooth encryption support for newer devices
- 🔄 Automatic encryption detection
- 🛡️ Backward compatibility with non-encrypted devices
- 🔧 Improved error handling and setup reliability

### Previous Versions
- Based on the original Patrick762/hassio-bluetti-bt integration
- Enhanced with encryption capabilities from bluetti-bluetooth-lib

## Contributing

Contributions are welcome! Please:
1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is based on the original hassio-bluetti-bt integration and includes enhancements for encryption support as provided by Bluetti's official bluetooth library.

## Credits

- Original integration by [Patrick762](https://github.com/Patrick762/hassio-bluetti-bt)
- Encryption support from [Bluetti Official](https://github.com/bluetti-official/bluetti-bluetooth-lib)
- Enhanced and maintained by the community
