#!/usr/local/bin/python3
"""Contains settings to use with get_modem_settings.py"""

NETWORKS = [
    '10.228.16.0/20',
    '10.228.32.0/20',
    '10.228.48.0/20',
    '10.228.64.0/20',
    '10.228.80.0/20',
    '10.228.96.0/20'
]

MODELS = ['TG1662G', 'TG1672G', 'TG2472G', 'TG2472GP2', 'TG862G', 'TG3452A']

OUTFILE = 'host_config_data.csv'

FIELDNAMES = [
    'IP Address', 'MAC Address', 'Model', 'WAN Type', 'WAN IP',
    'WAN Subnet Mask', 'WAN Gateway IP', 'LAN IP', 'LAN Subnet Mask',
    'LAN DHCP Enabled', 'DHCP Start IP', 'DHCP End IP', 'NAT Type',
    '2G Wifi Enabled', '2G SSID', '2G SSID Broadcast', '2G Security Mode',
    '2G PSK', '5G SSID', '5G Wifi Enabled', '5G SSID Broadcast',
    '5G Security Mode', '5G PSK'
]

SWITCH = {
    'arrisRouterWanConnType': 'WAN Type',
    'ifPhysAddress.2': 'MAC Address',
    'sysName.0': 'Model',
    'ifOperStatus.10000': '2G Radio',
    'ifOperStatus.10001': '2G Wifi',
    'ifOperStatus.10100': '5G Radio',
    'ifOperStatus.10101': '5G Wifi',
    'arrisRouterWanStaticIPAddr': 'WAN IP',
    'arrisRouterWanStaticPrefix': 'WAN Subnet Mask',
    'arrisRouterWanStaticGateway': 'WAN Gateway IP',
    'arrisRouterLanGatewayIp': 'LAN IP',
    'arrisRouterLanSubnetMask': 'LAN Subnet Mask',
    'arrisRouterLanUseDHCP': 'LAN DHCP Enabled',
    'arrisRouterLanStartDHCP': 'DHCP Start IP',
    'arrisRouterLanEndDHCP': 'DHCP End IP',
    'arrisRouterLanPassThru': 'NAT Type',
    'arrisRouterBssSSID.10001': '2G SSID',
    'arrisRouterBssSSID.10101': '5G SSID',
    'arrisRouterBssSSIDBroadcast.10001': '2G SSID Broadcast',
    'arrisRouterBssSSIDBroadcast.10101': '5G SSID Broadcast',
    'arrisRouterBssSecurityMode.10001': '2G Security Mode',
    'arrisRouterBssSecurityMode.10101': '5G Security Mode',
    'arrisRouterWPAPreSharedKey.10001': '2G PSK',
    'arrisRouterWPAPreSharedKey.10101': '5G PSK',
    }
