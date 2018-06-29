#!/usr/local/bin/python3
"""
Test module get_wan_info
"""

import csv
from ipaddress import IPv4Network
from easysnmp import Session
import config
from utils import ping_host
from snmp_getters import get_lan_info, get_sys_info, get_wan_info, get_wifi_info
from mongo_ops import store_doc, find_doc

def main():
    """main function"""
    # networks = [IPv4Network(x) for x in config.NETWORKS]
    networks = [IPv4Network('10.228.80.0/28')]
    outfile = config.OUTFILE
    fieldnames = config.FIELDNAMES

    # If output file is specified, initialize the file to 
    # contain only a header.
    if outfile:
        with open(outfile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    for network in networks:
        for host in network:
            host_info = {}
            if ping_host(host):
                # Query the host for config
                host_info = query_host(host)

                if not host_info:
                    continue

                host_info['IP Address'] = str(host)

                # Write results to csv if output file was specified
                if outfile:
                    with open(outfile, 'a', newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow(host_info)

                # Store in db
                if not find_doc(host_info['MAC Address']):
                    doc_id = store_doc(host_info)
                    print(doc_id)
                else:
                    print("Modem exists")
            else:
                print('{} no response'.format(str(host)))

def query_host(host):
    """Return host config data

    Sets up the SNMP session, processes the query functions
    and returns host config data
    """
    functs = [get_sys_info, get_lan_info, get_wan_info, get_wifi_info]
    community_str = 'public'
    ver = 2
    host_info = {}
    session = Session(str(host), community=community_str, version=ver)

    for func in functs:
        data = func(session)
        if not data:
            return 0
        host_info.update(data)
    return host_info

if __name__ == '__main__':
    main()
