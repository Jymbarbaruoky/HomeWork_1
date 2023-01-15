from collections import UserDict
from datetime import datetime
import pickle
import re

# клас батько, для роботи з данними 
class Field:
    def __init__(self, value: str):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        
# клас нащадок, зберігає ім'я контакту, то провіряє на валідність   
class Name(Field):
    
    @Field.value.setter
    def value(self, name: str):
        if name.isnumeric():
            raise ValueError('Wrong name')
        self._value = name


a = Name('Bob')
b = Field('hgf')


print(b.__class__.__name__)
