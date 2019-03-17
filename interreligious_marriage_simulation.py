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
    person1.marital_status = True
    person2.marita_status = True
    person1.spouse = person2
    person2.spouse = person1

class Person():
    def __init__(self, religion, gender, marital_status=False, spouse=None):
        self.religion = religion
        self.gender = gender
        self.marital_status = marital_status
        self.spouse = spouse

p1 = Person(religion='islam', gender= 'male')
p2 = Person(religion='islam', gender = 'female')
marry(p1, p2)

def generate_random_religion(religions=['islam', 'non-islam'], p = [0.5, 0.5], n=100):
    assert sum(p) == 1
    assert len(religions) == len(p)
    assert len(religions) > 1
    religions_of_populations = []
    #how to make a list of randomly generated religion
    return religions_of_populations

population1 = []
n_of_person = 100
for i in range(n_of_person):
    person = Person(religion='islam', gender= 'male')
    population1.append(person)














