```portScanner/06_webSecurity/SQL injection/README.md
# SQL Injection Tools

This directory contains scripts and utilities related to SQL Injection exploitation and analysis, with a focus on Time-Based Blind SQL Injection techniques.

## Attribution

The code, concepts, and methodologies implemented in this directory are based on examples and recipes from the **Python Web Penetration Testing Cookbook**.

## Contents

- **jitter.py**: A utility script designed to calculate the average response time (latency) of a target web server.
    - **Purpose**: Establishing a reliable baseline is critical for Time-Based SQL Injection. It allows the attacker to distinguish between normal network jitter/latency and a successful database `SLEEP()` or delay command.
    - **Usage**: `python3 jitter.py <url>`

---

**Disclaimer**: These tools are for educational purposes and authorized testing only. Do not use them on systems you do not own or have explicit permission to test.
