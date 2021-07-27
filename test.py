import requests

isValid = False

while not isValid: 
        height = input("Insert Combined Height In Inches: ")
        if height:
            aux = int(height)
            if aux >= 120 and aux <= 200:
                isValid = True
                print(f"These are the Pair Of NBA players who match the Added height: ")
                response = requests.get('https://mach-eight.uc.r.appspot.com/').json()
                players = response['values']
                for i in players:
                    for j in players: 
                        if int(i['h_in']) + int(j['h_in']) == aux:
                            print(i['first_name'], i['last_name'], j['first_name'], j['last_name'])
            else:
                print('The height entered must be a valid number between 120 and 200')
        else:
                print('Input can not be empty')


