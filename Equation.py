# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:26:10 2018

@author: Himansh
"""

import numpy as np
import sympy as sp
import math as m
rho = sp.Symbol("rho")
phi = sp.Symbol("phi")
z = sp.Symbol("z")
x = sp.Symbol("x")
y = sp.Symbol("y")
theta = sp.Symbol("theta")
r = sp.Symbol("r")
def carToCyl(cartesian):
    cylindrical = [0,0,0]
    cylindrical[0] = (cartesian[0].subs({x:rho*sp.cos(phi),y:rho*sp.sin(phi),z:z})*(sp.cos(phi))) + (cartesian[1].subs({x:rho*sp.cos(phi),y:rho*sp.sin(phi),z:z})*sp.sin(phi))
    cylindrical[1] = (cartesian[0].subs({x:rho*sp.cos(phi),y:rho*sp.sin(phi),z:z})*(-sp.sin(phi))) + (cartesian[1].subs({x:rho*sp.cos(phi),y:rho*sp.sin(phi),z:z})*sp.cos(phi))
    cylindrical[2] = cartesian[2]
    return cylindrical
def carToSph(H_rect):
    H_sph = [0,0,0]
    H_sph[0] = (H_rect[0].subs({x:r*sp.sin(theta)*sp.cos(phi),y:r*sp.sin(theta)*sp.sin(phi)}))*((sp.sin(theta)*sp.cos(phi))+(sp.cos(theta)*sp.cos(phi))-sp.sin(phi))
    H_sph[1] = (H_rect[1].subs({x:r*sp.sin(theta)*sp.cos(phi),y:r*sp.sin(theta)*sp.sin(phi)}))*((sp.cos(theta)*sp.cos(phi))+(sp.sin(theta)*sp.cos(phi))+sp.cos(phi))
    H_sph[2] = (H_rect[2].subs({x:r*sp.sin(theta)*sp.cos(phi),y:r*sp.sin(theta)*sp.sin(phi)}))*(sp.cos(theta)-sp.sin(theta))
    return H_sph