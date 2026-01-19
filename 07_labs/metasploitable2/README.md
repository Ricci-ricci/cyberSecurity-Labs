# Metasploitable 2

Metasploitable 2 is an intentionally vulnerable Linux virtual machine. This VM is designed to be used as a target for testing security tools and practicing penetration testing techniques in a safe, legal environment. It is maintained by Rapid7, the same company behind the Metasploit Framework.

## What is Metasploitable 2?

Metasploitable 2 serves as a "punching bag" for security professionals and students. It comes pre-configured with a large number of vulnerabilities, including:

- **Weak Passwords:** Default or easily guessable credentials on services like SSH, Telnet, and MySQL.
- **Vulnerable Services:** Older versions of vsftpd, Apache Tomcat, distcc, Samba, and more, which have known RCE (Remote Code Execution) exploits.
- **Web Applications:** It hosts several vulnerable web applications such as **DVWA** (Damn Vulnerable Web App) and **Mutillidae**, allowing practice of SQL injection, XSS, and file inclusion attacks.
- **Misconfigurations:** Open ports and services that should not be exposed (e.g., NFS shares, rlogin).

**Warning:** Never expose Metasploitable 2 to an untrusted network (like the open internet). It is easily compromised. Use it only in a Host-Only or NAT network configuration within your virtualization software (VirtualBox, VMware).