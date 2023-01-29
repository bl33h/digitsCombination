#/**
 #* *Copyright (C), 2023-2024, Sara Echeverria (bl33h)
    # *@author Sara Echeverria, Melissa Perez, Fabian Juarez, Andres Montoya, Ricardo Mendez, Adrian Rodriguez
    # *FileName: digitsCombination
    # @version: I
    #- Creation: 25/01/2023
    #- Last modification: 28/01/2023

# Library import
from itertools import permutations, combinations_with_replacement, product
from collections import Counter

# Data
digits = [0,1,2,3,4,5,6,7,8,9]

# Section A
# Generate all 4 digit sequences
sequences = list(permutations(digits, 4))
# Print the sequences count
print("\nA.) The count of all 4 digit sequences is:", len(sequences))

# Section B
# Generate all 4 digit sequences with one or more repeated elements
repeatedElementsSequences = list([x for x in product(digits, repeat = 4) if len(set(x))<4])
print("B.) The count of all 4 digit sequences with one or more repeated elements is:", len(repeatedElementsSequences))

# Section C
# C1
# Generate all 4 digit sequences with the same 4 elements
allRepeatedSequences = list(combinations_with_replacement(digits, 1))
print("C1.) The count of all 4 digit sequences with the same 4 elements is:", len(allRepeatedSequences))

# C2
# Get all 4 digit sequences where two digits are repeated twice
fourRepeatedSequences = [x for x in product(digits, repeat = 4) if all(val == 2 for val in Counter(x).values())]
print("C2.) The count of all 4 digit sequences where two digits are repeated twice is:", len(fourRepeatedSequences))

# C3
# Get all 4 digit sequences where one element is repeated twice and the other two are not
twoRepeatedSequences = [x for x in product(digits, repeat = 4) if len(set(x)) == 3]
print("C3.) The count of 4 digit sequences where one element is repeated twice and the others two don't repeat:", len(twoRepeatedSequences))

# C4
# Get all 4 digit sequences where one element is repeated twice and the other two are not
threeRepeatedSequences = list([x for x in product(digits, repeat = 4) if x.count(x[0]) == 3 or x.count(x[1]) == 3 or x.count(x[2]) == 3 or x.count(x[3]) == 3])
print("C4.) The count of all 4 digit sequences with one element repeated 3 times and the other one is not:", len(threeRepeatedSequences))

# Verification that the sum of the items in Section C are equal to the value obtained in Section B
totalSum = len(allRepeatedSequences) + len(fourRepeatedSequences) + len(twoRepeatedSequences) + len(threeRepeatedSequences)

if totalSum == len(repeatedElementsSequences):
    print("\nThe verification is successful and the sum of the items in Section C are equal to the value obtained in Section B!\n")
else:
    print("\nThe verification failed! The sum of the items in Section C are't equal to the value obtained in Section B.\n")