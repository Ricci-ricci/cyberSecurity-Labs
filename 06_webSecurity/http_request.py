import urllib.parse
import urllib.request
from io import BytesIO

# from me Ricci
# i get all the code from the book "Black hat Python 2nd Edition" by Justin Seitz so i really
# recommend you to buy it if you want to learn more about web security and pentesting
# This file demonstrates basic HTTP interaction:
# - Sending GET and POST requests (urllib and requests)
# - Reading HTTP responses as bytes/text
# - Parsing HTML responses to extract links (lxml + BeautifulSoup)
import requests
from bs4 import BeautifulSoup
from lxml.etree import etree

URL = "http://example.com"
info = {"name": "ricci", "passwd": "superpasswd"}

# -----------------------------
# urllib: basic GET request
# -----------------------------
# urlopen(URL) issues a GET request by default.
# response.read() returns the raw HTTP response body as bytes.
with urllib.request.urlopen(URL) as response:
    content = response.read()
    print(content)

# -----------------------------
# urllib: basic POST request
# -----------------------------
# To make a POST request with urllib:
# 1) URL-encode the payload (dict -> "name=...&passwd=...")
# 2) Convert it to bytes (HTTP bodies are bytes on the wire)
# 3) Pass it as `data` to Request(...) which switches the method to POST.
data = urllib.parse.urlencode(info).encode("utf-8")
req = urllib.request.Request(URL, data)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print(content)

# -----------------------------
# requests: GET and POST
# -----------------------------
# requests.get/post return a Response object:
# - .text  -> decoded text (based on headers/encoding detection)
# - .content -> raw bytes from the response body
responseGET = requests.get(URL)
print(responseGET.text)

responsePOST = requests.post(URL, data=info)
print(responsePOST.text)

# -----------------------------
# Parsing HTML bytes with lxml
# -----------------------------
# Here we fetch the page and parse the raw bytes as HTML using lxml.
# BytesIO wraps the bytes so etree.parse() can read it like a file.
# Then we search for all <a> tags and print their href attributes.
r = requests.get(URL)
content1 = r.content  # raw bytes of the HTML response body

parser = etree.HTMLParser()
noByte = BytesIO(content1)  # treat bytes like a file object
content2 = etree.parse(noByte, parser)

for link in content2.findall(".//a"):
    print(link.get("href"))

# -----------------------------
# Parsing HTML text with BeautifulSoup
# -----------------------------
# BeautifulSoup works nicely with the decoded string response (.text).
# We parse the HTML and then find all <a> tags, printing their hrefs.
r2 = requests.get(URL)
soup = BeautifulSoup(r2.text, "html.parser")

for link in soup.findAll("a"):
    print(link.get("href"))
