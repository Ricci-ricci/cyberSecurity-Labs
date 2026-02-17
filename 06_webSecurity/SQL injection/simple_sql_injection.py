"""
Simple SQL Injection Detection Script

This script attempts to detect SQL injection vulnerabilities by sending a single quote (')
as a payload. It checks the response for specific database error messages that indicate
the input was processed as SQL commands rather than data.

Database signatures checked:
- MySQL
- MSSQL (Native Client)
- PostgreSQL (Syntax Error)
- Oracle (ORA)

-----------------------------------------------------------------------------------------
WARNING: DO NOT USE ANY SCRIPT IN AN ENVIRONMENT YOU DO NOT OWN OR HAVE EXPLICIT
PERMISSION TO TEST.
-----------------------------------------------------------------------------------------
"""

import requests

url = "http://127.0.0.1/SQL/sqli_labs_master/Less-1/index.php?id="
initial = "'"
print(f"Testing SQL Injection on {url} with initial payload: {initial}")

r = requests.get(url + initial)

if "mysql " in r.text.lower():
    print("SQL injectable Detected with the initial payload!")
elif "native client " in r.text.lower():
    print("Injectable MSSQL detected with the initial payload!")
elif "syntax error" in r.text.lower():
    print("Injectable Postgress detected with the initial payload!")
elif "ORA" in r.text.lower():
    print("Injectable Oracle detected with the initial payload!")
else:
    print("No SQL Injection vulnerability detected with the initial payload.")
