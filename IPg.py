#!/usr/bin/env python3
"""
IPg v0.0

API :  https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=8.8.8.8

IPg receives two values as arguments: the file and the API key
IPg.py <file path> <API key>

"""
import sys
import requests
import os

# global variable. modifiable depending on the data you want to obtain
API_DATA = ["ip","country_name","state_prov","city","isp",] 
API_URL = "https://api.ipgeolocation.io/ipgeo" 

def geolocate_file(ip_list, key):
    """use the arguments provided by the user to make the request

    Args:
        ip_list (array): array of IP addresses obtained from a text file
        key (string): API key
    """
    for ip in ip_list:
        r = requests.get(f"{API_URL}?apiKey={key}&ip={ip}")
        data = r.json()

        #output function
        output(data)

def geolocate_ip(ip, key):
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
    
   
