
# PortScanner
PortScanner is a Python-based network security tool that allows users to scan ports on a given host. It provides multiple scanning modes, including predefined scans for localhost, user-defined port ranges, specific port lists, and full-range scans.





## Features

- Scan all ports of IP 
- Scan user-defined IP and ports
- Scan specific port lists
- Scan a user-specified port range
- Interactive menu for user input





## Requirements
- Python 3.x
- colorama module

### Install Dependencies
To install the required dependencies, run:

`pip install colorama`



## Usage/Examples
Run the script using:

`python3 portscanner.py`

Then follow the interactive menu to choose the desired scanning mode.

## How It Works

1. The script prompts the user to choose a scanning mode.
2. Based on the selection, the script scans the specified IP and port range.
3. Results are displayed with color-coded output:

* Red: Closed ports

* Green: Open ports

## Menu Options
`[1] Scan all ports of IP 127.0.0.1 `

`[2] Enter IP and scan a range of ports`

`[3] Enter IP and specify a list of ports`

`[4] Enter IP and specify a range of ports`

`[5] Enter IP and scan all ports (1-65535)`

`[6] Exit`


# Notes

### Ensure you have the necessary permissions to run port scans on the target system.

### Running full scans on external hosts without permission may violate security policies.
