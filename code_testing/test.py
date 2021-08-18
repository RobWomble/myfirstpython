#!/usr/bin/env python3
""" Author: Rob Womble
    testing how functions affect variables """

def inc_var(x):
    x += 1
    return x

def run_var():
    x = 1
    x = inc_var(x)
    print(x)

run_var()
