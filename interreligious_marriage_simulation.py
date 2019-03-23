#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:28:05 2019

@author: alifahsanul
"""

"""
Answering the question: for given probability, how will the population become when interreligion marriage happen. Muslim men can marry non muslim, but muslim women can't marry non muslim men
"""

import numpy as np
np.random.seed(42)

def marry(person1, person2):
    if person1.gender == person2.gender: raise ValueError('no lgbt')
    if person1.gender == 'male' and person1.religion != 'islam' and person2.religion == 'islam': person1.religion = 'islam'
    if person2.gender == 'male' and person2.religion != 'islam' and person1.religion == 'islam': person2.religion = 'islam'
    person1.marital_status = True
    person2.marital_status = True
    person1.spouse = person2
    person2.spouse = person1

class Person():
    def __init__(self, religion, gender, marital_status=False, spouse=None):
        self.religion = religion
        self.gender = gender
        self.marital_status = marital_status
        self.spouse = spouse

p1 = Person(religion='jew', gender= 'male')
p2 = Person(religion='islam', gender = 'female')
marry(p1, p2)

def generate_random_religion(religions=['islam', 'non-islam'], p = [0.7, 0.3], n=100):
    assert sum(p) == 1
    assert len(religions) == len(p)
    assert len(religions) > 1
    religions_of_populations = np.random.choice(religions, n, True, p)
    return religions_of_populations

def generate_random_gender(p = [0.5, 0.5], n=100):
    assert sum(p) == 1
    assert len(p) ==2
    genders = np.random.choice(['male', 'female'], n, True, p)
    return genders

population1 = []
n_of_person = 100
for i in range(n_of_person):
    person = Person(religion='islam', gender= 'male')
    population1.append(person)

a = generate_random_religion()
b = generate_random_gender()
print(b)












