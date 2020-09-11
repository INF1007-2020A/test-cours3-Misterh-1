#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
        new_letter = []
    new_name = ''
    for j in range(len(nom)):
        letter_num = ord(nom[j])
        if j == 0 :
            if letter_num >= 97 and letter_num <= 122 :
                letter_num = letter_num - 32
        else :
            if letter_num >= 65 and letter_num <= 90 :
                letter_num = letter_num + 32
        num_letter = chr(letter_num)
        new_letter.append(num_letter)
        new_name = new_name + new_letter[j]
        #print(new_name)
    nom = new_name
    return nom


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
