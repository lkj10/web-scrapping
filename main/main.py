import requests

answer = 'n'

while True:
    if answer == 'y':
        break
    elif answer == 'n':
        print("Welcome to IsItDown.py!")
        print("Please write a URLs you want to check. (separated by comma)")
        b = input()
        for x in b.split(','):
            x = x.strip()
            if x[-4:] != '.com':
                print(f"{x} is not a vaild URL.")
            else:
                if x[0:7] != 'http://':
                    x = 'http://' + x
                try:
                    url = requests.get(f'{x}')
                    if(url.status_code == 200):
                        print(f"{x} is up!")
                    else:
                        print(f"{x} is down!")
                except:
                    print(f"{x} is down!")
        print("Do you want to start over? y/n")
        answer = input()
        continue
