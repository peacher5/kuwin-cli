# KUWiN CLI
A command-line tool for login/logout Kasetsart University Wireless Network (KUWiN) without CAPTCHA.

## Introduction
It uses the same protocol as the [KUWiN Tools](https://play.google.com/store/apps/details?id=th.ac.ku.kuwintools) (Official App on Android) that's no CAPTCHA required for authentication. You can use this tool when you're in KU Network only. (Wifi, LAN, VPN, or whatever)

## Features
- List your login sessions including IP and login date/time.
- Login & logout from KU Network.
- Logout from all sessions.

## Requirement
- Python 3.x

## Usage
```
$ python kuwin.py <action> <username> <password>
```

## Actions
- list
- login
- logout
- logout-all

## Example
```
$ python kuwin.py login b6010987654 mypassword
```
