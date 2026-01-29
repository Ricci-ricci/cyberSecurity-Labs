# 06 - Web Security

## Disclaimer & Attribution

All scripts in this module are created for **learning purposes only** and are intended to be used **only on systems you own or have explicit permission to test**.

This module’s scripts and exercises are based on concepts and techniques referenced from the book **Black Hat Python (2nd Edition)**.

This module contains tools and scripts dedicated to assessing the security of web applications.

## Overview

Web applications are often the primary entry point for attackers due to their accessibility and complexity. This directory covers the use of Python to interact with web servers, analyze HTTP traffic, and identify common web vulnerabilities.

## Topics Covered

- **HTTP Interaction**: Using libraries like `requests` and `urllib` to send custom HTTP requests and analyze responses.
- **Header Analysis**: Inspecting HTTP headers for security configurations (e.g., CSP, X-Frame-Options, HSTS).
- **Directory Brute-forcing**: scripts to discover hidden paths and files on a web server.
- **Basic Vulnerability Scanning**: Introduction to detecting issues like SQL Injection or Cross-Site Scripting (XSS) through pattern matching in responses.

## Tools and Libraries

- **`requests`**: The standard for making HTTP requests in Python.
- **`BeautifulSoup`**: For parsing HTML and extracting data from web pages.

## Goal

To understand the client-server interaction of the web and how to automate the discovery of security flaws in web applications.