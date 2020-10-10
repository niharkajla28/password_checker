import requests

if __name__ == '__main__':
    url = 'https://api.pwnedpasswords.com/range/' + '5CEC1'
    res = requests.get(url)
    print(res)