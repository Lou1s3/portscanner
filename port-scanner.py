#!/usr/bin/python3
#
#Python Port-Scanner.
#
#Autora: Emmanuelle Corrá.
#
#Versão: 1.0.0.

import socket
import threading
import concurrent.futures
import argparse

print_lock = threading.Lock()

ip = input('Adicione o endereço IP para o escaneamento': )

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(f'{port} Está aberta')
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port +1)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--ports", action="store",  help="Irá indicar a quantidade de portas para serem escaneadar.")
    parser.add_argument("-t", "--ip", action="store", help="O target é o endereço de IPV4. Caso não exista um IPV4, não terá como identificar se a porta está aberta.")
    parser.add_argument("-o", "--lock", action="store", help="Vai fazer com que não seja indicada mais de 1 porta ao mesmo tempo, fazendo com que não embaralhe.)")
    args = parser.parse_args()
    
    get_arguments
