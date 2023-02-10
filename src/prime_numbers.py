

import numpy as np
import pandas as pd


def is_prime(number):
    """
    Check if the given number is prime or not.
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_primes_in_range(start, end):
    """
    Get all the prime numbers between the given start and end range.
    """
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)


    #This is some random usages of np and pd
    d = {'previous_costs': np.random.randint(0,100,size=6), 'new_costs': np.random.randint(0,100,size=6)}
    df = pd.DataFrame(data=d)
    print(df)

    return prime_numbers
