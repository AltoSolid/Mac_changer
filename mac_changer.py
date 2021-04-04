#!/usr/bin/env python
import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--i", dest="interface", type=str, required=True, help="Interface to change it's current MAC Address")
    parser.add_argument("--m", dest="mac", type=str, required=True, help="new MAC Address")
    return parser.parse_args() 


def change_mac(interface, new_mac):
    print("[+] Changing MAC addres for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


results = get_arguments()
change_mac(results.interface, results.mac)

