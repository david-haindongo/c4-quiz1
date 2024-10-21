#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:41:17 2024

@author: user
"""
import pandas

country_file = pandas.read_csv("country_data.csv")
dia_file = pandas.read_csv("diab_data.csv")
housing_file = pandas.read_csv("housing_data.csv")
insurance_file = pandas.read_csv("insurance_data.csv")
iris_file = pandas.read_csv("iris.csv")

print(country_file)