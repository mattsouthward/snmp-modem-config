#!/usr/local/bin/python3
"""
Test module get_wan_info
"""

import csv
from ipaddress import IPv4Network
from easysnmp import Session
import config
import db
from utils import ping_host
from snmp_getters import get_lan_info, get_sys_info, get_wan_info, get_wifi_info

def main():
    """main function"""
    networks = [IPv4Network(x) for x in config.NETWORKS]
    # networks = [IPv4Network('10.228.80.96/28')]
    outfile = config.OUTFILE
    fieldnames = config.FIELDNAMES

    # If output file is specified, initialize the file to
    # contain only a header.
    if outfile:
        with open(outfile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    for network in networks:
        hosts = network.hosts()
        for host in hosts:
            host = str(host)
            host_info = {}
            if ping_host(host):
                # Query the host for config
                host_info = query_host(host)

                if not host_info:
                    continue

                host_info['IP Address'] = host

                # Write results to csv if output file was specified
                if outfile:
                    with open(outfile, 'a', newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow(host_info)

                # Store host_info in db if it isn't already, replace it
                # if it is.
                updated_doc = db.MODEMS.find_one_and_replace(
                    {'MAC Address': host_info['MAC Address']},
                    host_info,
                    projection={'MAC Address': True, '_id': False},
                    upsert=True
                )

                print('{} found. Replacing'.format(updated_doc['MAC Address'])
                      if updated_doc
                      else
                      '{} not found. Inserting.'.format(host_info['MAC Address'])
                     )

            else:
                print('{} no response'.format(host)) # REMOVE IN PRODUCTION

def query_host(host):
    """Perform SNMP queries on host and return host config data."""
    functs = [get_sys_info, get_lan_info, get_wan_info, get_wifi_info]
    community_str = 'public'
    ver = 2
    host_info = {}
    session = Session(host, community=community_str, version=ver)

    for func in functs:
        data = func(session)
        if not data:
            return 0
        host_info.update(data)
    return host_info

if __name__ == '__main__':
    main()
