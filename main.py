# Password check pawen
import requests
import hashlib
import sys


input_password= input('Input Password that you want to check: ')


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(response.text)
    return get_password_leaks_count(response, tail)


def main(password):
    if password:
        count = pwned_api_check(password)
        if count:
            print(f'Your {password} was found {count} times...you should change your password')
        else:
            print(f'Your {password} was NOT found, is´s safe. Carry on')


main(input_password)

