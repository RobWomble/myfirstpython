#!/usr/bin/env python3
""" Alta3 Research | Rob Womble
    11Aug2021 Homework Assignment 3
    counting grades                """


def main(grades):
    A = 0
    B = 0
    C = 0
    D = 0
    F = 0
    for grade in grades:
        if int(grade) >= 90:
            A += 1
        elif int(grade) >= 80:
            B += 1
        elif int(grade) >= 70:
            C += 1
        elif int(grade) >= 60:
            D += 1
        else:
            F += 1
    grade_count = {'A' : A, 'B' : B, 'C' : C, 'D' : D, 'F' : F}
    print(grade_count)


grade_entry = input("please enter scores as integers from 0-100, separated by commas: ").split(',')
main(grade_entry)
