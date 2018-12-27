# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 20:01:18 2018

@author: Himansh
"""

import Equation as eq
import sympy as sp
x = sp.Symbol("x")
y = sp.Symbol("y")
z = sp.Symbol("z")
cartesian = [3*x,4*y,5*z]
print(eq.carToCyl(cartesian))
print(eq.carToSph(cartesian))
