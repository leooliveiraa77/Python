# CLI de utilidades capaz de executar diferentes tarefas
# criar um arquivo JSON e salvar na pasta correta
# Converter JSON para CSV
# listar e ordenar os dados
# Validar CPF/CNPJ para compra
# implementar Argparse Module

import argparse
import csv
import json
from pathlib import Path

parser = argparse.ArgumentParser(usage='python cli-utilidades.py <--name NAME>', description= 'This is a Toolkit for a car dealer where you can manage a bunch of tools like update storage, create files and validated documents')
parser.add_argument('--name', help='your name')

args = parser.parse_args()

if args.name:
    print(f'Hello {args.name}! We are glad to see you here')
else:
    print(f'Hello! We are glad to see you here')

#Modelos em estoque
cars = [{'brand': 'Chevrolet', 'model': 'chevette', 'year':1977},
        {'brand': 'BYD', 'model': 'dolphin', 'year':2025},
        {'brand': 'Haval', 'model': 'H6 GT', 'year':2025}]


def initApp():

    user_input = input('TOOLKIT for car dealership: add, list, save, csv, buy: (exit to close) ').lower()

    if user_input == 'add':
        add_car()
    elif user_input == 'save':
        save_cars()
    elif user_input == 'csv':
        convert_csv()
    elif user_input == 'list':
        list_cars()
    elif user_input == 'buy':
        buy_cars()
    elif user_input == 'exit':
        print('bye!')
        return
    else:
        print('Type a valid entry')
        initApp()

def add_car():
    user_car_Input = input('Type separed by commas \',\': brand, model, year: ')
    if user_car_Input == '' or user_car_Input.lower() == 'exit':
        initApp()

    user_car_Input_arr = user_car_Input.replace(' ', '').split(',')

    #validating input
    if not len(user_car_Input_arr) == 3:
        print('Invalid entry')
        add_car()


    cars.append({'brand': user_car_Input_arr[0], 'model': user_car_Input_arr[1], 'year': int(user_car_Input_arr[2])})
    print('Done!\n')
    print(cars)
    add_car()

def save_cars():
    base_dir = Path(__file__).parent
    file_path = base_dir / 'cars.json'
    with open( file_path, 'w', encoding='utf-8') as file:
        json.dump(cars, file, ensure_ascii= False, indent= 4)
    print('Saved!')
    initApp()

def convert_csv():
    data = None
    #ensures the correct file path.
    base_dir_json = Path(__file__).parent
    file_path_json = base_dir_json / 'cars.json'

    try:
        with open(file_path_json, 'r', encoding='utf-8') as file:
            data = json.load(file)

    except FileNotFoundError:
        print('File not Found')

    if not isinstance(data, list) or not data:
        initApp()

    #ensures the correct file path.
    base_dir_csv = Path(__file__).parent
    file_path_csv = base_dir_csv / 'cars.csv'
    
    try:
        with open(file_path_csv, 'w', newline= '',encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames= data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print("CSV file successfully created!")
    except FileNotFoundError:
        print('File not Found')
    initApp()

def list_cars(type=True):
    user_list_type = input('Sorted or All? ').lower() if type == True else 'sorted'
    data_car_list = None
    idx = 1

    if user_list_type == 'all':
        data_car_list = cars        
    elif user_list_type == 'sorted':
        data_car_list = sorted(cars, key= lambda car: car['year'], reverse=True)
    elif user_list_type == '' or user_list_type == 'exit':
        initApp()
    else:
        print('invalid entry')
        list_cars()
    
    for el in data_car_list:
        print(f'{idx} car: {el['model']} by {el['brand']}, year {el['year']}')
        idx += 1
    idx = 1
    initApp()

def buy_cars():
    user_id = input('type here your CPF or CNPJ without dots or commas (ex: 12345678901): ')

    if user_id == '' or user_id == 'exit':
        initApp()    
    elif not user_id.isdigit():
        print('Enter with numbers only!')
        buy_cars()
    elif len(user_id) == 11 or len(user_id) == 14:
        if user_id == user_id[0] * 11:
            print('invalid doc')
            buy_cars()
        else:
            print('valid doc! Take a look on our cars \n')
            list_cars(False)
    else:
        print('invalid format')
        buy_cars()



initApp()

