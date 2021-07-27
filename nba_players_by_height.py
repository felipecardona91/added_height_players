import requests #se importa requests para poder hacer llamados a apis

isValid = False #bandera para el mientras, control de acceso a este. 

while not isValid: #mientras no sea valido, entra. 
        height = input("Insert Height In Inches: ") #insercion del dato de altura, entra como string
        if height: #comienza validacion de datos ingresados por consola
            aux = int(height) #se convierte el dato ingresado a numero para poder validarlo
            if aux >= 60 and aux <= 100: #el valor debe de estar entre estaturas en inches usualmente reales
                isValid = True #si se da esto, la bandera se pone en true
                print(f"These are the NBA players who match the heigh: ") #comienza la impresion del encabezado de los datos de los juagadores
                response = requests.get('https://mach-eight.uc.r.appspot.com/').json() #se traen los datos de la api e inmediatamente se convierten en json, en este paso es un dict
                for key in response.values(): #se itera sobre el json, en este caso llamado values, se accede al valor de este por medio del metodo values()
                    for i in key: #se itera sobre cada value
                        if i['h_in'] == height: #se comprueba que el valor en la posicion de altura de jugador sea igual a la altura ingresada. 
                            print(i['first_name'], i['last_name']) #imprimo el nombre y apellido del jugador
            else:
                print('The height entered must be a valid number between 60 and 100')
        else:
                print('Input can not be empty')

