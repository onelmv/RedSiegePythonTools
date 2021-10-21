#!/usr/bin/env python3
"""
IPg v0.0

API :  https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY&ip=8.8.8.8

IPg receives two values as arguments: the file and the API key
IPg.py <file path> <API key>

"""
import sys
import requests

# global variable. modifiable depending on the data you want to obtain
API_DATA = ["ip","country_name","state_prov","city","isp",] 
API_URL = "https://api.ipgeolocation.io/ipgeo" 

def geolocate(ip_list, key):
    """use the arguments provided by the user to make the request

    Args:
        ip_list (array): array of IP addresses obtained from a text file
        key (string): API
    """
    for ip in ip_list:
        r = requests.get(f"{API_URL}?apiKey={key}&ip={ip}")
        data = r.json()

        #output function
        output(data)

def output(data):
    #TODO improve the output format
    """Print the data 
        
    Args:
        data (array): data contain the API data in json format
    """
    print("================================")
    i = 0
    for elem in data:
        if elem == API_DATA[i]:
            print(f"{elem}:{data[elem]}")
            i += 1
            if i == 5 : break # this break here it to avoid an overflow

def main(argv):
       
    # this array will contain all the ip addresses 
    ip_list = []
    with open(argv[1], 'r') as iFile:
       for ip in iFile:
           ip_list.append(ip)

    geolocate(ip_list, argv[2])

if __name__ == "__main__":
    # making sure the 2 arguments is present. 
    if len(sys.argv) == 3:
        main(sys.argv)
    else:    
        print("Format : IPg.py <file path> <API key>")
    
   
