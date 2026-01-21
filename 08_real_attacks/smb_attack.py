"""
Chapter studied: Violent Python – SMB exploitation

Objective:
Understand how attackers identify and exploit vulnerable SMB services.

Steps studied:
1. Scan target for open SMB ports (445)
2. Enumerate SMB version
3. Identify known vulnerabilities
4. Understand exploitation workflow via frameworks

Important note:
Exploitation was performed only in a controlled lab environment.
No exploit code or payloads are included.
"""

import nmap


def findTarget(subnet):
    nmapScan = nmap.PortScanner()
    # scan for subnet in port 445
    print(f"Scanning for SMB services on subnet {subnet} on port 445")
    nmapScan.scan(hosts=subnet, ports="445")
    tgtHosts = []

    # loop through all host
    for host in nmapScan.all_hosts():
        if nmapScan[host].has_tcp(445):
            state = nmapScan[host]["tcp"][445]["state"]
            if state == "open":
                print("[+] Found target host" + host)
                tgtHosts.append(host)
    return tgtHosts


def setupHandler():
    # We will not put any exploit here cause it s only for learning purpose
    pass
