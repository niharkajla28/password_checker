import requests
import hashlib
import sys

if __name__ == '__main__':


    def request_api_data(query_char):
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        # if res.status_code != 200:
        #     raise RuntimeError(f'Error fetching: {res.status_code}, check the api and check again')
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
        return get_password_leaks_count(response, tail)


    def main_func(args):
        for item in args:
            check = pwned_api_check(item)
            if check:
                print(f'Your password: {item} is compromised {check} times.')
            else:
                print(f'Your password: {item} is not compromised.')

    def input_from_file():
        with open('input_pass.txt', 'r') as input_file:
            for item in input_file.readlines():
                passwords_list = item.split()

            main_func(passwords_list)


    input_from_file()

    