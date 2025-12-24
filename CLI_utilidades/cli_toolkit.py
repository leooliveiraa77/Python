# CLI de utilidades capaz de executar diferentes tarefas
# criar um arquivo JSON e salvar na pasta correta
# Converter JSON para CSV
# Contar palavras, linhas e caracteres de um arquivo
# Renomear arquivos em lote
# Validar CPF/CNPJ

import json
import csv

#Modelos em estoque
cars = [{'brand': 'Chevrolet', 'model': 'chevette', 'year':1977},
        {'brand': 'BYD', 'model': 'dolphin', 'year':2025},
        {'brand': 'Haval', 'model': 'H6 GT', 'year':2025}]

def initApp():
    user_input = input('TOOLKIT for car dealership: add, save, csv: ').lower()

    if user_input == 'add':
        add_car()
    elif user_input == 'save':
        save_car()
    elif user_input == 'csv':
        convert_csv()

def add_car():
    user_car_Input = input('type separed by commas \',\': brand, model, year: ').lower()
    if user_car_Input == '' or user_car_Input == 'exit':
        initApp()

    user_car_Input_arr = user_car_Input.replace(' ', '').split(',')
    cars.append({'brand': user_car_Input_arr[0], 'model': user_car_Input_arr[1], 'year':user_car_Input_arr[2]})
    print('Done!\n')
    print(cars)
    add_car()

def save_car():
    with open('cars.json', 'w', encoding='utf-8') as file:
        json.dump(cars, file, ensure_ascii= False, indent= 4)
    print('Saved!')
    initApp()

def convert_csv():
    try:
        with open('cars.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
    finally:
        print("No such file or directory: 'cars.json'")

initApp()

