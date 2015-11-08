# -*- coding: utf-8 -*-
import random
import string
import time

Prenom1 = input("Prenom de la premiere personne (sans espaces/caracteres speciaux) : ")
Nom1 = input("Nom de la premiere personne (sans espaces/caracteres speciaux) : ")
Prenom2 = input("Prenom de la deuxieme personne (sans espaces/caracteres speciaux) : ")
Nom2 = input("Nom de la deuxieme personne (sans espaces/caracteres speciaux) : ")

print("Calculs de Compatibilité en cours...")
time.sleep(random.uniform(2.5, 4.5))
print("Calculs terminés.")
time.sleep(0.3)
print("Mise en forme des resultats...")
time.sleep(random.uniform(1.5, 3.5))
print("Mise en forme terminées.")
time.sleep(0.5)

LastLetterNumber = 0
Somme = 0

num2alpha = dict(zip(string.ascii_lowercase, range(1, 27)))
for i in range(len(Prenom1)):
    LetterNumber = num2alpha[Prenom1[i]]
    while LetterNumber > 9:
        LetterNumber -= 9
    # print("Letter Number =",LetterNumber)
    Somme = LastLetterNumber + LetterNumber
    # print("Somme =",Somme)
    LetterA = str(Somme)
    LetterA = LetterA[0]
    if Somme <= 9:
        LetterB = "0"
    else:
        LetterB = str(Somme)
        LetterB = LetterB[1]
    LastLetterNumber = int(LetterA) + int(LetterB)
    # print(LastLetterNumber)

Prenom1Num = LastLetterNumber
# print("Prenom1 =", Prenom1Num)

###################################################################
###################################################################
###################################################################

LastLetterNumber = 0
Somme = 0

num2alpha = dict(zip(string.ascii_lowercase, range(1, 27)))
for i in range(len(Nom1)):
    LetterNumber = num2alpha[Nom1[i]]
    while LetterNumber > 9:
        LetterNumber -= 9
    # print("Letter Number =",LetterNumber)
    Somme = LastLetterNumber + LetterNumber
    # print("Somme =",Somme)
    LetterA = str(Somme)
    LetterA = LetterA[0]
    if Somme <= 9:
        LetterB = "0"
    else:
        LetterB = str(Somme)
        LetterB = LetterB[1]
    LastLetterNumber = int(LetterA) + int(LetterB)
    # print(LastLetterNumber)

Nom1Num = LastLetterNumber
# print("Nom1 =", Nom1Num)

###################################################################
###################################################################
###################################################################


LastLetterNumber = 0
Somme = 0

num2alpha = dict(zip(string.ascii_lowercase, range(1, 27)))
for i in range(len(Prenom2)):
    LetterNumber = num2alpha[Prenom2[i]]
    while LetterNumber > 9:
        LetterNumber -= 9
    # print("Letter Number =",LetterNumber)
    Somme = LastLetterNumber + LetterNumber
    # print("Somme =",Somme)
    LetterA = str(Somme)
    LetterA = LetterA[0]
    if Somme <= 9:
        LetterB = "0"
    else:
        LetterB = str(Somme)
        LetterB = LetterB[1]
    LastLetterNumber = int(LetterA) + int(LetterB)
    # print(LastLetterNumber)

Prenom2Num = LastLetterNumber
# print("Prenom2 =", Prenom2Num)

###################################################################
###################################################################
###################################################################

LastLetterNumber = 0
Somme = 0

num2alpha = dict(zip(string.ascii_lowercase, range(1, 27)))
for i in range(len(Nom2)):
    LetterNumber = num2alpha[Nom2[i]]
    while LetterNumber > 9:
        LetterNumber -= 9
    # print("Letter Number =",LetterNumber)
    Somme = LastLetterNumber + LetterNumber
    # print("Somme =",Somme)
    LetterA = str(Somme)
    LetterA = LetterA[0]
    if Somme <= 9:
        LetterB = "0"
    else:
        LetterB = str(Somme)
        LetterB = LetterB[1]
    LastLetterNumber = int(LetterA) + int(LetterB)
    # print(LastLetterNumber)

Nom2Num = LastLetterNumber
# print("Nom2 =", Nom2Num)

###################################################################
###################################################################
###################################################################

SommePrenoms = Prenom1Num + Prenom2Num
SommeNoms = Nom1Num + Nom2Num

Char1 = str(SommePrenoms)
Char1 = Char1[0]
if SommePrenoms > 9:
    Char2 = str(SommePrenoms)
    Char2 = Char2[1]
else:
    Char2 = "0"

Personne1Number = int(Char1) + int(Char2)

Char1 = str(SommeNoms)
Char1 = Char1[0]
if SommeNoms > 9:
    Char2 = str(SommeNoms)
    Char2 = Char2[1]
else:
    Char2 = "0"

Personne2Number = int(Char1) + int(Char2)

# print(Personne1Number)
# print(Personne2Number)

if Personne1Number > Personne2Number:
    difference = Personne1Number - Personne2Number
elif Personne1Number < Personne2Number:
    difference = Personne2Number - Personne1Number
else:
    difference = 0
Percent = (-25 / 2) * difference + 100
print("Le pourcentage de compatibilité entre", Prenom1, Nom1, "et", Prenom2, Nom2, "est de :", str(int(Percent)) + "%")
