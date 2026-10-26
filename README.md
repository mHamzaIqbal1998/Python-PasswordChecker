# Password Checker 🔐

A simple command-line tool that checks whether your passwords have appeared in known data leaks, using the [Pwned Passwords API](https://haveibeenpwned.com/Passwords) from [Have I Been Pwned](https://haveibeenpwned.com/).

## How it works

The script never sends your actual password anywhere. It:

1. Hashes your password with **SHA-1**
2. Sends only the **first 5 characters** of that hash to the API
3. The API returns a list of all leaked password hashes that start with those same 5 characters
4. The script then looks for your password's full hash **locally on your machine**

This technique (called **k-anonymity**) means your real password never leaves your computer.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)

Install the dependency with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line, passing one or more passwords as arguments:

```bash
python3 checkmypass.py <password1> <password2> ...
```

### Example

```bash
$ python3 checkmypass.py hello password123 MyS3cureP@ss
hello was found 362615 times, you should change it
password123 was found 287566 times, you should change it
MyS3cureP@ss was NOT found, Carry on!
```

## Output

- **Found** — the password exists in known data breaches (the number shows how many times it has been seen). You should change it!
- **NOT found** — the password does not appear in known leaks. That doesn't guarantee it's safe, but it's a good sign.

## License

This project is for educational purposes — feel free to use and modify it.
