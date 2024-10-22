import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# finde the max value in an array

def my_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

list = [1, 2, 3, 4, 5, 66, 7, 8, 9, 10]
print(my_max(list)) 

# using max function

print("max function used", max(list))


