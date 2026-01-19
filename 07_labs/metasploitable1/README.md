# Metasploitable 1

Metasploitable 1 is the original intentionally vulnerable Linux virtual machine created by the Metasploit team.

## Overview

While now considered legacy compared to Metasploitable 2 and 3, version 1 was the pioneer in providing a safe sandbox for security professionals to test the Metasploit Framework. It offers a snapshot of the security landscape from the mid-2000s.

## Key Features

- **Legacy Vulnerabilities:** Contains older service vulnerabilities that are rarely seen in modern environments but are fundamental for understanding the history of exploitation.
- **Services:** Includes vulnerable versions of services like Samba, Apache, and distcc.

## Usage

This VM is distributed as a VMware image. Like its successors, it should **never** be exposed to an untrusted network or the internet. It is intended for use in a host-only or NAT networking environment.

**Note:** For most modern learning paths, Metasploitable 2 is the recommended starting point, but Metasploitable 1 remains a useful archival resource.