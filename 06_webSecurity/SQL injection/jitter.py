"""
Jitter Utility for Time-Based SQL Injection

Why create a jitter for time-based SQL injection?

1. Evasion (WAF/IDS/IPS Bypass):
   Security appliances often look for automated patterns. If an attacker sends requests
   at perfectly regular intervals (e.g., exactly every 1.0 seconds), it is a clear signature
   of a bot or script. Introducing "jitter" (random variations in the delay between requests)
   makes the traffic look more like human interaction and less like an automated attack,
   reducing the likelihood of getting blocked.

2. Accuracy in Noisy Networks:
   Time-based SQL injection relies on the database pausing for a specific amount of time
   (e.g., SLEEP(5)) to confirm a True condition. However, network latency and server load
   can cause natural fluctuations in response time. Understanding and calculating network
   jitter allows the script to distinguish between a genuine database sleep command and
   standard network lag, reducing false positives.

-----------------------------------------------------------------------------------------
WARNING: DO NOT USE ANY SCRIPT IN AN ENVIRONMENT YOU DO NOT OWN OR HAVE EXPLICIT
PERMISSION TO TEST.

Unauthorized testing, scanning, or exploitation is illegal and unethical. These educational
materials are provided for learning purposes only, to help security professionals understand
vulnerabilities and defend against them.
-----------------------------------------------------------------------------------------
"""

import sys

import requests

url = sys.argv[1]

values = []
for i in range(100):
    r = requests.get(url)
    values.append(r.elapsed.total_seconds())

average = sum(values) / float(len(values))

print("average response time: {}".format(average))
