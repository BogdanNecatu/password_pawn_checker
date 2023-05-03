# Password check pawen
import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes=(line.split(':') for line in hashes.text)
    for h, count in hashes:
        print

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail, response)
    return get_password_leaks_count(response, tail)


pwned_api_check('password')
