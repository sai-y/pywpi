#!/usr/bin/python3

import random

if __name__ == "__main__":
    while True:
        rand_num = random.randrange(0,10)
        input_value = int(input("Enter a number between 0 and 10: "))
        if input_value == rand_num:
            print("Your guess is correct! You win!")
            break
        else:
            print("Nope! The random value was %s" % rand_num)

        
        

