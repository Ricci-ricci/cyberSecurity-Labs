# 02 - Port Scanning

This module focuses on the core mechanics of port scanning using Python.

## Overview

Port scanning is the process of attempting to connect to a range of ports on a target system to determine which services are listening. This directory explores different techniques and improvements to basic scanning.

## Topics Covered

- **Basic TCP Scanning**: Using `socket.connect()` to determine if a port is open.
- **Handling Timeouts**: Ensuring the scanner doesn't hang on unresponsive ports.
- **Error Handling**: Managing socket errors and connection refusals gracefully.
- **Multi-threading**: Speeding up the scanning process by probing multiple ports simultaneously.

## Usage

Scripts in this directory can typically be run by providing a target IP address and a range of ports to scan.
