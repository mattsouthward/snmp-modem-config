#!/usr/local/bin/python3
"""Contains the MIBs to query modems for."""

WAN = [
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterWanConnType.0',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterWanStaticIPAddr.1',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterWanStaticPrefix.1',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterWanStaticGateway.1'
]

SYS = [
    'ifPhysAddress.2',
    'sysName.0',
    'ifOperStatus.10000',
    'ifOperStatus.10001',
    'ifOperStatus.10100',
    'ifOperStatus.10101'
]

LAN = [
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterLanGatewayIp.200',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterLanSubnetMask.200',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterLanUseDHCP.200',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterLanStartDHCP.200',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterLanEndDHCP.200',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterLanPassThru.200'
]

WIFI = [
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterBssSSID.10101',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterBssSSID.10001',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterBssSSIDBroadcast.10001',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterBssSSIDBroadcast.10101',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterBssSecurityMode.10001',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterBssSecurityMode.10101',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterWPAPreSharedKey.10001',
    'ARRIS-ROUTER-DEVICE-MIB::arrisRouterWPAPreSharedKey.10101'
]
