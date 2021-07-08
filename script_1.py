#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json
import requests
import time

print("\033[96m")
print("")
print("5SIM.NET SCRIPT")
print("")
print("")

Attivazione = False

# variabii

token = input("Scrivi qui la tua api key: ")
country = input("Scrivi qui la regione da cui prendere il numero [in inglese]: ")
operator = input("Scrivi qui l'operatore del numero [scrivi any se per te è uguale]: ")
product = input("Scrivi qui per cosa userai questo numero [esempio: telegram]: ")

# funzioni
def get_code():
    r = json.loads(requests.get('https://5sim.net/v1/user/check/' + str(dio["id"]), headers={
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }).text)
    if len(r['sms']) == 0:
        return False
    else:
        try:
            for message in r['sms']:
                if message["sender"].lower() == "telegram":
                    print("Code: ", message["code"])
        except KeyError:
            return False

# codice
if input("Vuoi iniziare ? [si/no]: ").lower() == "si":
    print("Quando starterai partirà un ciclo infinito e non smetterà finchè non prende il numero")
    if input("Vuoi startare il grab? [si/no]: ").lower() == "si":
        Attivazione = True
        while Attivazione:
            try:
                dio = json.loads(requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers={
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
        }).text)
                print("Numero: " + str(dio["phone"]))
                print("!Attendere il codice di attivazione!")
                Attivazione = False
                get_code()
                print("\033[0m")
                while get_code() == False:
                    time.sleep(0.10)
                    pass
            except:
                print("Numero non presente nel database / saldo insufficente... ora continuo con le richieste")
                print("\033[0m")
                time.sleep(0.5)