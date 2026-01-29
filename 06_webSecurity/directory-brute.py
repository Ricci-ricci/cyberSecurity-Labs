"""
Directory brute forcer (learning purpose)

What it does:
- Loads a wordlist of potential paths (admin, images, login, etc.)
- Builds URL candidates (/, /word/, /word.php, /word.bak, ...)
- Makes HTTP GET requests to the target for each candidate
- Prints "hits" (200 OK) and optionally interesting codes (301/302/403/etc.)

Notes:
- Always use this ONLY on systems you own or have explicit permission to test.
- This is a simple, educational implementation (not optimized for stealth).
"""

import os
import queue
import sys
import threading

import requests

# User-Agent header used for all HTTP requests (some servers block empty/unknown agents)
AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"

# Extensions to try for each word in the wordlist (e.g., admin.php, backup.bak, etc.)
EXTENSIONS = [".php", ".bak", ".orig", ".inc"]

# Base URL to brute force. Keep no trailing slash for consistent concatenation.
TARGET = "http://testphp.vulnweb.com"

# Wordlist file (default: a file located next to this script).
# If you want a custom path, replace the value or pass a full path here.
WORDLIST = os.path.join(os.path.dirname(__file__), "common.txt")

# Number of worker threads
THREADS = 5

# Network safety: avoid hanging forever on slow servers
TIMEOUT_SECONDS = 5

# If True, prints 404 lines too (not very useful, but good for learning)
VERBOSE_404 = False


def get_words(resume: str | None = None) -> queue.Queue:
    """
    Load words from the wordlist file and enqueue URL candidates.

    resume:
      If provided, skip words until this one is found (useful if you stop mid-way
      and want to continue where you left off).
    """
    words: queue.Queue[str] = queue.Queue()

    def extend_words(word: str) -> None:
        # If the word already contains a dot, treat it as a file (e.g., robots.txt)
        if "." in word:
            words.put(f"/{word}")
        else:
            # Otherwise treat it as a directory first (e.g., /admin/)
            words.put(f"/{word}/")

        # Also try common file extensions for each word (e.g., admin.php, admin.bak)
        for ext in EXTENSIONS:
            words.put(f"/{word}{ext}")

    # Fail early with a clear message if the wordlist is missing
    if not os.path.exists(WORDLIST):
        raise FileNotFoundError(
            f"Wordlist not found: {WORDLIST}\n"
            "Create it (one path per line) or update WORDLIST to point to an existing file."
        )

    with open(WORDLIST, "r", encoding="utf-8", errors="ignore") as f:
        raw_words = f.read()

    found_resume = resume is None
    for word in raw_words.splitlines():
        word = word.strip()
        if not word or word.startswith("#"):
            # Skip empty lines and comments
            continue

        if not found_resume:
            if word == resume:
                found_resume = True
                print(f"[i] Resuming wordlist from: {resume}")
            continue

        extend_words(word)

    return words


def dir_bruter(words: queue.Queue) -> None:
    """
    Worker function run by each thread.

    Pulls items from the shared Queue until empty, requests each URL,
    and prints interesting responses.
    """
    headers = {"User-Agent": AGENT}

    while not words.empty():
        path = words.get()
        url = f"{TARGET}{path}"

        try:
            # We use a timeout so a slow or unresponsive server doesn't hang a thread forever.
            r = requests.get(url, headers=headers, timeout=TIMEOUT_SECONDS)
        except requests.exceptions.ConnectionError:
            # Connection errors happen if the host is down, blocked, or network is unstable.
            sys.stderr.write("x")
            sys.stderr.flush()
            continue
        except requests.exceptions.Timeout:
            # Timeout indicates the server was too slow to respond.
            sys.stderr.write("t")
            sys.stderr.flush()
            continue

        # Basic interpretation of results:
        # - 200 usually means "found"
        # - 301/302 often indicates a real path that redirects (also interesting)
        # - 403 means forbidden but the path likely exists
        # - 404 means not found (usually not interesting unless debugging)
        if r.status_code == 200:
            print(f"[+] {r.status_code} {url}")
            sys.stderr.write("+")
            sys.stderr.flush()
        elif r.status_code == 404:
            if VERBOSE_404:
                print(f"[-] {r.status_code} {url}")
            sys.stderr.write(".")
            sys.stderr.flush()
        elif r.status_code in (301, 302, 307, 308, 401, 403):
            print(f"[!] {r.status_code} {url}")
            sys.stderr.write("!")
            sys.stderr.flush()
        else:
            print(f"[?] {r.status_code} {url}")
            sys.stderr.write("?")
            sys.stderr.flush()


if __name__ == "__main__":
    # Queue up candidate paths
    words = get_words()
    print(f"[i] Target: {TARGET}")
    print(f"[i] Wordlist: {WORDLIST}")
    print(f"[i] Threads: {THREADS}")
    print("Press return to continue...")
    sys.stdin.readline()

    # Start worker threads
    for _ in range(THREADS):
        t = threading.Thread(target=dir_bruter, args=(words,), daemon=True)
        t.start()

    # Wait for all threads to finish
    for t in threading.enumerate():
        if t is not threading.current_thread():
            try:
                t.join()
            except RuntimeError:
                # Some threads may already be finished; ignore join errors safely.
                pass
