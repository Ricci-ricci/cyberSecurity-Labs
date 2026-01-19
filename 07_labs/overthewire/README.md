# OverTheWire Wargames

OverTheWire (OTW) provides a series of free, online wargames designed to help you learn and practice security concepts in a fun, addictive way. Unlike the Metasploitable VMs, you do not download these labs; you connect to them remotely (usually via SSH).

## Why OverTheWire?

- **Zero Setup:** No need to configure VMs or networks. You just need a terminal and an SSH client.
- **Progressive Difficulty:** Levels start very easy and get progressively harder. Each level gives you the password for the next level.
- **Community:** It is one of the most popular starting points for CTF (Capture The Flag) players.

## Recommended Wargames

### 1. Bandit (The Absolute Basics)
**Start here!** Bandit is designed for absolute beginners.
- **Goal:** Learn the Linux command line.
- **Skills:** `ls`, `cd`, `cat`, file permissions, SSH, piping, and searching text.
- **Format:** You SSH into `bandit0` and find the password for `bandit1` hidden in a file.

### 2. Leviathan
Often the next step after Bandit.
- **Goal:** Introduction to binary exploitation and Linux privileges.
- **Skills:** SUID binaries, basic debugging, and command injection.

### 3. Natas
A web-security focused wargame.
- **Goal:** Learn server-side web security.
- **Skills:** Inspecting HTML source, HTTP headers, authentication bypass, PHP vulnerabilities, and SQL injection.

### 4. Krypton
- **Goal:** Learn cryptography.
- **Skills:** Ciphers, frequency analysis, and breaking weak encryption.

## How to Play

1. Go to the [OverTheWire website](https://overthewire.org/).
2. Select a wargame (e.g., Bandit) on the left menu.
3. Read the instructions for Level 0.
4. Open your terminal and connect:
   ```bash
   ssh bandit0@bandit.labs.overthewire.org -p 2220
   ```
5. Enter the password provided on the site.
6. Solve the challenge to get the password for the next level (bandit1).