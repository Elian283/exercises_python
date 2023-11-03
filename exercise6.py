# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:21:34 2023

@author: s_bartsch21
"""
def vokon_zählen(text):
    x_list = list(text.lower())  # Konvertiert den Text in Kleinbuchstaben und erstellt eine Liste der Zeichen
    vokale = 0
    konsonanten = 0

    for zeichen in x_list:
        if zeichen.isalpha():
            if zeichen in "aeiou":
                vokale += 1
            else:
                konsonanten += 1

    ergebnis = f"Anzahl Vokale: {vokale}, Anzahl Konsonanten: {konsonanten}"
    return ergebnis

text = "Berlin"
ergebnis = vokon_zählen(text)
print(ergebnis)




