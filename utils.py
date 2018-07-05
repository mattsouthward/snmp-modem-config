#!/usr/local/bin/python3
"""
Test module get_wan_info
"""

import subprocess
from ipaddress import IPv4Address, AddressValueError
import config

def convert_to_hex(val):
    """Return an uppercased hexidecimal string representation of val."""
    return bytes(val, 'latin-1').hex().upper()

def convert_to_ip(val):
    """Return an string representation of an IP address from val."""
    try:
        return str(IPv4Address(bytes(val, 'latin-1')))
    except AddressValueError:
        return 0

def pretty_keys(info):
    """Returns info dictionary with shortened keys."""
    return dict((config.SWITCH[k], info[k]) for k in info)

def ping_host(host):
    """
    Pings an ip addresses to determine if the host is active on the network.
    Ping options in subprocess.Popen are BSD-style options.
    Parameters:
    host - IP address of host to ping
    Returns:
    True if host responds, else False
    """
    devnull = subprocess.DEVNULL
    cmd_arr = ['ping', '-c', '1', '-W', '300', str(host)]
    result = subprocess.run(cmd_arr, stdout=devnull, stderr=devnull).returncode
    return True if result == 0 else False
