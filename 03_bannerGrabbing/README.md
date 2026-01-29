# 03 - Banner Grabbing

This directory contains scripts and tools specifically designed for Banner Grabbing.

## Overview

Banner grabbing is a technique used to gain information about a computer system on a network and the services running on its open ports. By capturing the initial message (the banner) sent by a service upon connection, security professionals can identify the software and specific version running.

## Topics Covered

- **Service Identification**: Extracting banners from open ports (FTP, SSH, HTTP, SMTP, etc.).
- **Vulnerability Mapping**: Using service versions to check for known CVEs (Common Vulnerabilities and Exposures).
- **Automated Collection**: Scripts to automatically connect and store banners from a list of targets.

## Importance

Knowing the specific version of a service is critical for both attackers and defenders.
- **Defenders** use it to identify outdated software that needs patching.
- **Attackers** use it to select specific exploits that work against that version.
