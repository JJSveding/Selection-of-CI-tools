import numpy as np
import pandas as pd


def Is_Prime(number):
    # Bad comment. This is a very looooooong comment. It will probably exceed the limit for a single row. Let's see if pylint picks this comment up.
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def getPrimesINRange(start, end):
    """
    Get all the prime numbers between the given start and end range.
    """
    prime_numbers = []
    for num in range(start, end + 1):
        if Is_Prime(num):
            prime_numbers.append(num)


    #This is some random usages of np and pd
    dataframe_with_a_very_long_name_that_causes_row_to_be_to_long = {'previous_costs': np.random.randint(0,100,size=6), 'new_costs': np.random.randint(0,100,size=6)}
    df = pd.DataFrame(data=dataframe_with_a_very_long_name_that_causes_row_to_be_to_long)
    print(df)

    return prime_numbers
