#!/usr/local/bin/python3
"""Contains settings to use with get_modem_settings.py"""

NETWORKS = [
    # Networks as string values in CIDR notation.
    # Ex. '192.168.0.0/24'
]

MODELS = [
    # Modem models to store data about
]

OUTFILE = 'host_config_data.csv'

FIELDNAMES = [
    # Fieldnames to use in csv file. Should match values in SWITCH.
]

SWITCH = {
    # Used to map long, cryptic mib names to friendlier names.
    # MIB names are the keys, values should match those in FIELDNAMES.
}
