# Metasploitable 3

Metasploitable 3 is the modern, highly extensive successor to Metasploitable 2. It represents a significant evolution in how vulnerable environments are built and deployed.

## Key Differences

Unlike versions 1 and 2, which were simple downloadable VM images, Metasploitable 3 is an automated build system.

- **Dual OS Support:** It allows you to build two different virtual machines:
  - **Windows Server 2008:** Providing a rare and valuable environment to practice attacking Windows-based services.
  - **Ubuntu 14.04:** A modern Linux environment with updated vulnerabilities.
- **Build Process:** It is built automatically using **Packer** (to create the image) and **Vagrant** (to manage the VM). This allows for easier updates and customization.

## Features

- **CTF Style:** It includes "flags" hidden throughout the system, gamifying the exploitation process.
- **Modern Vulnerabilities:** It covers a wider range of modern application vulnerabilities compared to the older versions.
- **Docker Support:** Some services run within Docker containers inside the VM, adding a layer of complexity relevant to modern infrastructure.

## Getting Started

Because this is not a simple download, setting it up requires installing:
1. Packer
2. Vagrant
3. A virtualization provider (VirtualBox or VMware)

Once the tools are installed, the environment is built via command line scripts provided in the official Rapid7 GitHub repository.

**Warning:** As with all vulnerable labs, keep these VMs on a Host-Only network. They are designed to be compromised.