# IPg

## Project 1 - The Scope!

Intermediate Task:  Have the script read multiple IP addresses from a text file and process them all at once.


__IPg receives two values as arguments: the file and the API key__

`Ipg.py <file> <API_key>`


API : https://ipgeolocation.io/documentation/ip-geolocation-api.html


## Output

================================

ip | country_name | state_prov | city | isp

## json response

```json
{
    "ip": "8.8.8.8",
    "hostname": "dns.google",
    "continent_code": "NA",
    "continent_name": "North America",
    "country_code2": "US",
    "country_code3": "USA",
    "country_name": "United States",
    "country_capital": "Washington, D.C.",
    "state_prov": "California",
    "district": "Santa Clara",
    "city": "Mountain View",
    "zipcode": "94043-1351",
    "latitude": "37.42240",
    "longitude": "-122.08421",
    "is_eu": false,
    "calling_code": "+1",
    "country_tld": ".us",
    "languages": "en-US,es-US,haw,fr",
    "country_flag": "https://ipgeolocation.io/static/flags/us_64.png",
    "geoname_id": "6301403",
    "isp": "Google LLC",
    "connection_type": "",
    "organization": "Google LLC",
    "asn": "AS15169",
    "currency": {
        "code": "USD",
        "name": "US Dollar",
        "symbol": "$"
    },
    "time_zone": {
        "name": "America/Los_Angeles",
        "offset": -8,
        "current_time": "2020-12-17 07:49:45.872-0800",
        "current_time_unix": 1608220185.872,
        "is_dst": false,
        "dst_savings": 1
    }
}
