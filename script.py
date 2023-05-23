import qrcode

# Data to encode: `WIFI:T:{security};S:{ssid};P:{password};;`

# Replace with your own details
ssid = 'Your_SSID'
password = 'Your_password'
security = 'WPA'  # or 'WEP', 'WPA2' etc.

wifi_info = f'WIFI:T:{security};S:{ssid};P:{password};;'

# Generate QR code
img = qrcode.make(wifi_info)

# Save QR code to a file
img.save('wifi_qrcode.png')
