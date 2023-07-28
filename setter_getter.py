#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Nov 17 14:07:23 2022

@author: Januario Cipriano
"""

from datetime import date


class Employee:
	def __init__(self, name, birth_date):
		self._name = name
		self._birth_date = birth_date

	@property
	def name(self):
		return self._name


	@name.setter
	def name(self, value):
		self._name = value.upper()

	@property
	def birth_date(self):
		return self._birth_date

	@birth_date.setter
	def birth_date(self, value):
		self._birth_date = date.fromisoformat(value)

	def __str__(self):
		return f'Person({self.name}, {self.birth_date})'

	def __repr__(self):
		return f'<Person:{self._name}:{self._birth_date}>'

john = Employee('John', '2001-02-07')
print(john)
john.name = 'John Doe'
print(repr(john))































