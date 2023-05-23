# WiFi QR Code Generator

## Description

This Python script uses the `qrcode` library to generate a WiFi QR code. The QR code created by the script, when scanned, will automatically connect the device to the specified WiFi network. 

The script requires three user inputs: 

1. SSID (name of the WiFi network)
2. Password (password to the WiFi network)
3. Security type (type of network security e.g., WPA, WEP, WPA2, etc.)

The generated QR code is saved as `wifi_qrcode.png` in the same directory where the script runs.

## Requirements

To run this script, you need:

- Python 3.6 or later
- `qrcode` Python library

## Setting up a Virtual Environment (venv)

A virtual environment is an isolated working copy of Python, allowing you to work on a specific project without affecting other projects.

To set up a virtual environment, follow the steps below:

### For Windows:
1. Open the command prompt (cmd.exe)
2. Navigate to the directory where you want the virtual environment to be set up.
3. Run `python -m venv venv` to create the virtual environment.
4. Activate the virtual environment with `.\venv\Scripts\activate`
5. Your command prompt should now show `(venv)` at the beginning of the line, indicating that you are now in a Python virtual environment.

### For Linux/MacOS:
1. Open the terminal
2. Navigate to the directory where you want the virtual environment to be set up.
3. Run `python3 -m venv venv` to create the virtual environment.
4. Activate the virtual environment with `source venv/bin/activate`
5. Your terminal should now show `(venv)` at the beginning of the line, indicating that you are now in a Python virtual environment.

## Installing Required Libraries

Once the virtual environment is set up and activated, you can install the required library, `qrcode`, using pip. 

Run `pip install qrcode` in your terminal/cmd.

## Running the Script

Before running the script, replace `'Your_SSID'`, `'Your_password'`, and `'WPA'` in the script with your actual WiFi SSID, password, and security type respectively. 

Once you've done that, you can run the script with `python3 script.py`. The generated QR code image will be saved in the same directory as `wifi_qrcode.png`.

## Disclaimer

Please ensure that you don't share the generated QR code with people you don't want to have access to your WiFi network, as anyone who scans the QR code will automatically be able to connect to the network.