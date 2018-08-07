#! /usr/bin/env python3.7

def func1(msg, tms=1):
    for i in range(tms):
        print(msg)

msg = input("Type the message to print - ").strip()
tms = int(input("Number of times you want to print it - "))
func1(msg)
