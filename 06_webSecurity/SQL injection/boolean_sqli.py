"""
Boolean-Based Blind SQL Injection Script

This script demonstrates how to extract data from a database when the application
does not return database errors or data directly (Blind SQLi).

Instead of seeing the data, we ask the database True/False questions.
If the application's response changes (e.g., different content length, different
text on the page) based on our question, we can infer the answer.

Mechanism:
1.  We inject a condition like `AND (SUBSTRING((SELECT database()), 1, 1) = 'a')`.
2.  If the first letter of the database name is 'a', the query returns TRUE, and the page loads normally.
3.  If it is not 'a', the query returns FALSE, and the page might miss some content or load differently.
4.  By iterating through all possible characters for each position, we reconstruct the data.

-----------------------------------------------------------------------------------------
WARNING: DO NOT USE ANY SCRIPT IN AN ENVIRONMENT YOU DO NOT OWN OR HAVE EXPLICIT
PERMISSION TO TEST.

Unauthorized testing, scanning, or exploitation is illegal and unethical. These educational
materials are provided for learning purposes only, to help security professionals understand
vulnerabilities and defend against them.
-----------------------------------------------------------------------------------------
"""
