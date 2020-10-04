#!/usr/local/bin/python3

# import requests module
from requests import request

# build the url request from a txt file
url_dict = {}

with open('txt-post-request-example/post-url-endpoint.txt') as url_file:
    for line in url_file:
        (key,val) = line.rstrip().split(', ')
        url_dict[key] = val

url = url_dict['hostname_path'] + '?post_endpoint=' + url_dict['post_endpoint'] + '&api_key=' + url_dict['api_key'] + '&api_output=' + url_dict['api_output']

# build the payload
payload_dict = {}

with open('txt-post-request-example/payload.txt') as payload_file:
    for line in payload_file:
        (key,val) = line.rstrip().split(', ')
        payload_dict[key] = val

# build the request header
header_dict = {}

with open('txt-post-request-example/header.txt') as header_file:
    for line in header_file:
        (key,val) = line.rstrip().split(', ')
        header_dict[key] = val

# execute request
response = request("POST", url, data = payload_dict, headers = header_dict)

# print response
print('\nresponse:')
print(response.text)