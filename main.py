# -*- coding: utf-8 -*-
import pandas as pd

def round_number(value):
    return round(value, 2)

titanic = pd.read_csv('titanic.csv')

# seleziona le tabelle survived and sex
titanic = titanic[['Sex', 'Survived']]
n_rows = float(titanic.shape[0])
n_survived = float((titanic['Survived'] == 1).sum())

#la probilità che uno sia sopravvissuto è:
p_survived = round_number(n_survived / n_rows)
p_not_survived = round_number(1 - p_survived)
#calcolo probabilità se una persona è sopravissuta essendo donna

n_female = float((titanic['Sex'] == 'female').sum())
n_male = n_rows - n_female

#probabilità sopravissuta essendo femmina
n_female_who_survived = titanic[(titanic['Sex'] == 'female') & (titanic['Survived'] == 1)].shape[0]

p_who_survived_given_woman = round_number(n_female_who_survived / n_female)

# PRINTER
print('--------------------------------------')
print('Number of passengers: ' + str(n_rows))
print('Prob survived: ' + str(p_survived))
print('Prob not survived: ' + str(p_not_survived))
print('Male: ' + str(n_male))
print('Female: ' + str(n_female))
print('Female who survived: ' + str(n_female_who_survived))
print('Who survived given woman: ' + str(p_who_survived_given_woman))
print('--------------------------------------')