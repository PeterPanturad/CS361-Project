import math
import itertools

# Constants ---------------------------------------------------------------

totalItems = 900000
falsePositiveRate = 0.01

# ------------------------------------------------------------------------- 

def get_h1(sha_string):                 # take first half of sha string and return as integer. usage: firstHalf = get_h1(sha_string)
    midpoint = len(sha_string) // 2
    first_half = sha_string[:midpoint] # split in python [beginning_of_split:end_of_split]

    return int(first_half, 16)          # converts hexadecimal number to decimal number and returns

def get_h2(sha_string):                 # take second half of sha string and return as integer. usage: secondHalf = get_h2(sha_string)
    midpoint = len(sha_string) // 2
    last_half = sha_string[midpoint:]

    return int(last_half, 16)           # converts hexadecimal number to decimal number and returns

def generate_indices(sha_string, k, m): # makes a list of k hashes of a password. usage: indices = generate_indicies(sha_string, k, m)
    h1 = get_h1(sha_string)
    h2 = get_h2(sha_string)

    indices = []    # empty list to add our indices calcukated inside

    for i in range(k):
        raw_hash = h1 + (i * h2)    #calculate raw hash based on double hash formula
        final_index = raw_hash % m  #apply mod to ensure index fits inside bit array
        indices.append (final_index)    #add index to list
    return indices

def sizeFilter(n, p):                   # calculate m = number of bits in array, k = number of hash functions and return. usage: m, k = sizeFilter(number of items to insert, false positive rate)
    m = math.ceil((-n * math.log(p)) / (math.log(2) ** 2))
    k = math.ceil((m/n) * math.log(2))
    return m, k

def readData(filename):                 # read from file and puts every new line into an array. usage: array = readData(filename)
    with open(filename, 'r') as file:
        dataArray = [line.strip() for line in file]

    return dataArray

def main(hexPasswords):
    n = totalItems
    p = falsePositiveRate
    m, k = sizeFilter(n, p)

    print(f"Total items to be inserted: {n}\nFalse Positive Rate = {p}\nNumber of bits in array: {m}\nNumber of hash functions: {k}\n")

if __name__ == "__main__":
    INPUT_FILE = 'processed_passwords.txt'

    hexPasswords = readData(INPUT_FILE)

    main(hexPasswords)
