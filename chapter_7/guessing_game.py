#!/usr/bin/python3

import random

if __name__ == "__main__":
    count = 0
    running_average = 0
    while True:
        rand_num = random.randrange(0,10)
        input_value = int(input("Enter a number between 0 and 10: "))
        if input_value == input_value:
            print("Your guess is correct! You win!")
            break

        
        

