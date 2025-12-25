# CLI de utilidades capaz de executar diferentes tarefas
# criar um arquivo JSON e salvar na pasta correta
# Converter JSON para CSV
# listar e ordenar os dados
# Validar CPF/CNPJ para compra

import json
import csv
from pathlib import Path

#Modelos em estoque
cars = [{'brand': 'Chevrolet', 'model': 'chevette', 'year':1977},
        {'brand': 'BYD', 'model': 'dolphin', 'year':2025},
        {'brand': 'Haval', 'model': 'H6 GT', 'year':2025}]

def initApp():
    user_input = input('TOOLKIT for car dealership: add, list, save, csv: ').lower()

    if user_input == 'add':
        add_car()
    elif user_input == 'save':
        save_cars()
    elif user_input == 'csv':
        convert_csv()
    elif user_input == 'list':
        list_cars()

def add_car():
    user_car_Input = input('type separed by commas \',\': brand, model, year: ').lower()
    if user_car_Input == '' or user_car_Input == 'exit':
        initApp()

    user_car_Input_arr = user_car_Input.replace(' ', '').split(',')
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
            print(data[0].keys())
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

def list_cars():
    user_list_type = input('Sorted or All? ').lower()
    data = None
    idx = 1

    if user_list_type == 'all':
        data = cars        
    elif user_list_type == 'sorted':
        data = sorted(cars, key= lambda car: car['year'], reverse=True)
    
    for el in data:
        print(f'{idx} car: {el['model']} by {el['brand']}, year {el['year']}')
        idx += 1
    idx = 1
    initApp()

initApp()

