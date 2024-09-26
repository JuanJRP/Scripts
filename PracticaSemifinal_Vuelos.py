#Librerias para funciones expecificas
import time
import os

#Funcion para el Menu, seleccion y validacion
def menu():
    os.system('cls')
    print('\n ___________________________________\n | 1. Agregar Pasajero.            |\n | 2. Agregar Pais.                |\n | 3. Agregar Ciudades.            |\n | 4. Filtrar ciudad por CC.       |\n | 5. Filtro pasajeros por ciudad. |\n | 6. Filtrar país por CC.         |\n | 7. Filtrar pasajeros por país.  |\n | 8. Ver Listas.                  |\n | 9. Salir del programa.          |\n ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n')
    try: 
        opc = int(input('Seleccione una opcion: '))
        if (opc > 9 or opc < 1): print(f'Opcion {opc} fuera de rango [1 - 9]'),time.sleep(2), menu()
        if opc == 1: addPassenger(ListPassenger, ListCountry, ListCities)
        if opc == 2: addCountry(ListCountry)
        if opc == 3: addCities(ListCities)
        if opc == 4: searchCities(ListPassenger)
        if opc == 5: searchNum_cities(ListPassenger)
        if opc == 6: searchCountry(ListPassenger)
        if opc == 7: searchNum_country(ListPassenger)
        if opc == 8: showList(ListPassenger, ListCountry, ListCities)
        if opc == 9: print('Salio Exitosamente.')     
    except Exception as e: print(f'Los datos ingresados son incorrectos\nCodigo de Error: {e}'), input('\nPresione una tecla para regresar al menu...'), menu()   

#Validacion de datos ingresados con las listas
def dataValidation(inputData, data):
    for fact in data:
        if inputData.lower() == fact.lower():
            return True
    return False

#Agregar pasajeros y validacion de datos con las informacion en las listas
def addPassenger(passengerList, countryList, citiesList):
    try:
        os.system('cls')
        name = str(input('Ingrese el nombre: ')).lower()
        Cc = int(input('Ingrese su CC: '))
        conutryDestination = str(input('Ingrese su pais de destino: ')).lower()
        if dataValidation(conutryDestination, countryList) == False: print(f'\nEl pais {conutryDestination} no se encuentra en la base de datos.\n'), input('\nPresione una tecla para regresar al menu...'), menu()
        else: citieDestination = str(input('Ingrese su ciudad de destino: ')).lower()
        if dataValidation(citieDestination, citiesList) == False: print(f'\nLa ciudad {citieDestination} no se encuentra en la base de datos.\n'), input('\nPresione una tecla para regresar al menu...'), menu()
        else:
            Passenger = (name, Cc, conutryDestination, citieDestination)
            passengerList.append(Passenger)
            os.system('cls')
            print(f'\nnombre: {name}\nCc: {Cc}\nPais de destino: {conutryDestination}\nCiudad de destino: {citieDestination}\n\nPasajero agregado exitosamente.\n')
            input('\nPresione una tecla para regresar al menu...')
            menu()
    except Exception as e: print(f'Los datos ingresados son incorrectos\nError: {e}'),input('\nPresione una tecla para regresar al menu...'), menu()

#Agregar Paises y verificacion
def addCountry(list):
    os.system('cls')
    country = (input('Ingrese el pais: ')).lower()
    if dataValidation(country, list) == True: print(f'\nEl pais {country} ya se encuentra en la base de datos.\n'), input('\nPresione una tecla para regresar al menu...'), menu()
    else: 
        list.append(country)
        print(F'El pais {country} fue agregado exitosamente\n')
        time.sleep(2)
        menu()

#Agregar ciudades y verificacion
def addCities(list):
    os.system('cls')
    cities = (input('Ingrese la ciudad: ')).lower()
    if dataValidation(cities, list) == True: print(f'\nLa ciudad {cities} ya se encuentra en la base de datos.\n'), input('\nPresione una tecla para regresar al menu...'), menu()
    else:
        list. append(cities)
        print(F'La ciudad {cities} fue agregada exitosamente\n')
        time.sleep(2)
        menu()

#Filtrado de ciudades a las que viaja un pasajero
def searchCities(cities):
    os.system('cls')
    CC = int(input('Ingrese el CC: '))
    for name, cc, country, citie in cities:
        if cc == CC:
            print("Nombre:", name)
            print("Cédula:", cc)
            print(f"Ciudad: {citie}\n")
    input('\nPresione una tecla para regresar al menu...')
    menu()

#Conteo del numero de pasajeros que viajan a una ciudad
def searchNum_cities(passenger):
    os.system('cls')
    citieName = input('Ingrese la ciudad: ').lower()
    count = 0
    for name, cc, country, citie in passenger:
        if citie.lower() == citieName.lower():
            count += 1
    print(f'\nLa cantidad de pasajeros que viajan a la ciudad es {count}\n')
    time.sleep(2)
    menu()

#Filtrado de paises a los que viaja un pasajero
def searchCountry(countrys):
    os.system('cls')
    CC = int(input('Ingrese el CC: '))
    for name, cc, country, citie in countrys:
        if cc == CC:
            print("Nombre:", name)
            print("Cédula:", cc)
            print(f"Pais: {country}\n")
    input('\nPresione una tecla para regresar al menu...')
    menu()

#Conteo del numero de pasajeros que viajan a un pais
def searchNum_country(passenger):
    os.system('cls')
    countryName = input('Ingrese el pais: ').lower()
    count = 0
    for name, cc, country, citie in passenger:
        if country.lower() == countryName.lower():
            count += 1
    print(f'\nLa cantidad de pasajeros que viajan al pais es {count}\n')
    time.sleep(2)
    menu()

#Muestra la informacion que contienen las listas
def showList(passengerList ,countryList, citiesList):
    os.system('cls')
    print(f'Lista de pasajeros\n')
    for name, cc, country, citie in passengerList:
        print("Nombre:", name)
        print("Cédula:", cc)
        print(f"Pais: {country}")
        print(f'Ciudad {citie}\n')
    print(f'___________________________________\n\nLista de paises\n')
    for country in countryList: print(f'{country}')
    print(f'___________________________________\n\nLista de ciudades\n')
    for citie in citiesList: print(f'{citie}')
    print('___________________________________\n')
    input('\nPresione una tecla para regresar al menu...')
    menu()

#Llenado de informacion predefinida
ListPassenger = [('David Velez', 70555952, 'USA', 'Boston'), ('Juan Porras', 8152612, 'España', 'Barcelona'), ('Clara López', 42722915, 'Colombia', 'Bogotá')]
ListCountry = [('USA'), ('España'), ('Colombia')]
ListCities = [('Boston'), ('Barcelona'), ('Bogota')]

#Inicio de programa, llamado al menu
menu()