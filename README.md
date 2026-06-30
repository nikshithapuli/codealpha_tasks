# Secure Coding Review

## Objective
Review a Python program to identify security weaknesses and provide a more secure version.

## Language
Python

## Vulnerabilities Found
- Hardcoded credentials
- Password visible while typing
- No password protection mechanism

## Improvements
- Used getpass to hide password input.
- Separated credentials into constants.
- Improved readability.

## Files
- vulnerable_code.py
- secure_code.py

## Conclusion
Secure coding practices reduce security risks and help protect sensitive information.