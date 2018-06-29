#!/usr/local/bin/python3
"""
Test module get_wan_info
"""

from easysnmp import EasySNMPError
from utils import convert_to_hex, convert_to_ip, pretty_keys
import settings
import mibs

def get_wan_info(session):
    """Test for function"""
    wan_types = {'1': 'dynamic', '2': 'static'}

    wan_info = process_mibs(mibs.WAN, session)

    # If process_mibs failed, return to caller
    if not wan_info:
        return 0

    wan_info['WAN Type'] = wan_types[wan_info['WAN Type']]
    wan_info['WAN IP'] = convert_to_ip(wan_info['WAN IP'])
    wan_info['WAN Gateway IP'] = convert_to_ip(wan_info['WAN Gateway IP'])

    return wan_info

def get_sys_info(session):
    """Return MAC address and model of the host from session."""
    sys_info = process_indexed_mibs(mibs.SYS, session)

    # If the process_indexed_mibs failed or if it returned a modem
    # model we don't care about return to the caller
    if not sys_info or sys_info['Model'] not in settings.MODELS:
        return 0

    # The following bool's set the 2G Wifi Enabled key to either True or
    # False. Only if both radio and 'wifi' are enabled in the modem
    # is the wireless actually enabled.
    sys_info['2G Wifi Enabled'] = bool(
        sys_info['2G Radio'] == '1' and sys_info['2G Wifi'] == '1')
    del sys_info['2G Radio']
    del sys_info['2G Wifi']

    sys_info['5G Wifi Enabled'] = bool(
        sys_info['5G Radio'] == '1' and sys_info['5G Wifi'] == '1')
    del sys_info['5G Radio']
    del sys_info['5G Wifi']

    sys_info['MAC Address'] = convert_to_hex(sys_info['MAC Address'])

    return sys_info

def get_lan_info(session):
    """Return LAN info of host from session."""
    nat_types = {
        '-1': 'unknown',
        '1': 'bridged',
        '2': 'routedWithNAT',
        '3': 'routedWithoutNAT'
    }

    lan_info = process_mibs(mibs.LAN, session)

    # if process_mibs failed, return to caller
    if not lan_info:
        return 0

    for i in lan_info:
        if i == 'NAT Type':
            lan_info[i] = nat_types[lan_info[i]]
        elif i == 'LAN DHCP Enabled':
            lan_info[i] = True if lan_info[i] == '1' else False
        else:
            lan_info[i] = convert_to_ip(lan_info[i])

    return lan_info

def get_wifi_info(session):
    """Return wireless info of host from session."""
    ssid_broadcast = {'2': False, '1': True}
    security_mode = {
        '0': 'disabled',
        '1': 'wep',
        '2': 'wpa-tkip',
        '3': 'wpa2-aes',
        '7': 'wpa/wpa2-tkip/aes'
    }
    enabled = {'1': True, '2': False}

    wifi_info = process_indexed_mibs(mibs.WIFI, session)

    # If process_indexed_mibs failed, return to caller
    if not wifi_info:
        return 0

    for i in wifi_info:
        if 'Security Mode' in i and wifi_info[i] != 'NOSUCHINSTANCE':
            wifi_info[i] = security_mode[wifi_info[i]]
        elif 'SSID Broadcast' in i and wifi_info[i] != 'NOSUCHINSTANCE':
            wifi_info[i] = ssid_broadcast[wifi_info[i]]
        elif 'Wifi Enabled' in i:
            wifi_info[i] = enabled[wifi_info[i]]
    if wifi_info['2G Security Mode'] == 'wep':
        wifi_info['2G PSK'] = 'Security mode is wep, update to psk'
    if wifi_info['5G Security Mode'] == 'wep':
        wifi_info['5G PSK'] = 'Security mode is wep, update to psk'

    return wifi_info

def process_indexed_mibs(mibs_list, session):
    """Return dictionary of indexed mibs and values."""
    info = {}

    for mib in mibs_list:
        try:
            result = session.get(mib)
        except EasySNMPError:
            return 0
        else:
            key = '{}.{}'.format(result.oid, result.oid_index)
            info[key] = result.value

    return pretty_keys(info)

def process_mibs(mibs_list, session):
    """Return dictionary of mibs and values."""
    info = {}

    for mib in mibs_list:
        try:
            result = session.get(mib)
        except EasySNMPError:
            return 0
        else:
            info[result.oid] = result.value

    return pretty_keys(info)
