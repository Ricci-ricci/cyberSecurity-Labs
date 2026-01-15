<file_path>
portScanner/08_real_attacks/README.md
</file_path>

<edit_description>
Create README.md for the new real attacks module
</edit_description>

# 08 - Real Attacks Demonstration

This module demonstrates real-world attack vectors and infection methods, such as the FTP-based k985ytv attack.

## Overview

These scripts are inspired by the book "Violent Python" by TJ O'Connor. I learned a lot from this book and highly recommend it: https://www.nostarch.com/violentpython.

In a recent massive compromise, dubbed k985ytv, attackers used anonymous and stolen FTP credentials to gain access to 22,400 unique domains and 536,000 infected pages (Huang, 2011). With access granted, the attackers injected javascript to redirect benign pages to a malicious domain in the Ukraine. Once the infected server redirected the victims, the malicious Ukrainian host exploited victims in order to install a fake antivirus program that stole credit card information from the clients. The k985ytv attack proved to be a resounding success. In the following section, we will recreate this attack in Python. Examining the FTP logs of the infected servers, we can see exactly what happened. An automated script connected to the target host in order to determine if it contained a default page named index.htm. Next the attacker uploaded a new index.htm, presumably containing the malicious redirection script. The infected server then exploited any vulnerable clients that visited its pages.

The goal is to show how real attacks work, including infection vectors, to better understand and defend against them.

## Disclaimer

**For Educational Purposes Only.** Do not use these scripts on systems you do not own or have explicit permission to test. Real attacks like K985ytv can cause significant harm, and replicating them without authorization is illegal.

## Topics Covered

- **Infection Vectors**: Examples of how malware spreads, like the FTP-based k985ytv attack's methods.
- **Exploit Demos**: Simplified scripts showing vulnerable code or attack techniques.
- **Defense Insights**: Understanding these helps in building better security.

## Usage

Run the scripts in a controlled environment only.

*Note: Ensure you have authorization before testing any exploits.*