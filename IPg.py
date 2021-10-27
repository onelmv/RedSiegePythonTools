#!/usr/bin/env python3
"""
IPg v0.0

API :  https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=8.8.8.8

IPg receives two values as arguments: the file and the API key
IPg.py <file path> <API key>

"""
import os
import sys
import requests
import ipaddress


# global variable. modifiable depending on the data you want to obtain
API_DATA = ["ip","country_name","state_prov","city","isp",]
API_URL = "https://api.ipgeolocation.io/ipgeo"

def geolocate_cidr(ip, key):
    #storing the ip without the CIDR
    if '\n' in ip:
        ip = ip.split('\n') # discaring '\n' at the end of the ip address
        ip = ipaddress.IPv4Network(ip[0]) # taking just the first part of the split
    else:
        ip = ipaddress.IPv4Network(ip) 

    ip_address = ip.network_address
    while ip_address <= ip.broadcast_address:
        data = requests.get(f"{API_URL}?apiKey={key}&ip={ip_address}").json()
        output(data)
        print(ip_address)
        ip_address += 1 #next ip on the network


def geolocate_file(ip_list, key):
     #request information from a list of IP addresses obtained from a text file

    for ip in ip_list:
        if '/' in ip:
            # if the IP addres is in CIDR format
            geolocate_cidr(ip, key)
        else:
            r = requests.get(f"{API_URL}?apiKey={key}&ip={ip}")
            data = r.json()

            #output function
            output(data)

def geolocate_ip(ip, key):

    if '/' in ip:
        # if the IP addres is in CIDR format
        geolocate_cidr(ip, key)
    else:
        #request information of a specific IP provided by the user.
        data = requests.get(f"{API_URL}?apiKey={key}&ip={ip}").json()

        output(data)

def output(data):
    """Print the data
       output : ip, country_name, state_prov, city, isp
    """
    print("================================")

    # message in case the ip address are not correct.
    if len(data) == 1:
        print("[!] IP NOT FOUND")
        print("[!] check IP addresses")
        print("[!] check your key")

    i = 0
    for elem in data:
        if elem == API_DATA[i]:
            print(f"{elem}:{data[elem]}")
            i += 1
            if i == 5 : break # this break here it to avoid an overflow

def main(argv):
    # check if it's a file with the IP addresses or a typed ip
    if os.path.isfile(argv[1]):
        # this array will contain all the ip addresses
        ip_list = []

        with open(argv[1], 'r') as iFile:
            for ip in iFile:
                ip_list.append(ip)
        geolocate_file(ip_list, argv[2])

    else:
        geolocate_ip(argv[1], argv[2])

if __name__ == "__main__":
    # making sure the 2 arguments is present.
    if len(sys.argv) == 3:
        main(sys.argv)
    else:
        print("Format : IPg.py <file path> <API key>")
        print("Format : IPg.py <IP address> <API key>")