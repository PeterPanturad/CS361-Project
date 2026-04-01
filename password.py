import math
import itertools

# Constants ---------------------------------------------------------------

totalItems = 900000
falsePositiveRate = 0.01

# ------------------------------------------------------------------------- 

def get_h1(sha_string):                 # take first half of sha string and return as integer. usage: get_h1(sha_string)
    midpoint = len(sha_string) // 2
    first_half = sha_string[:midpoint] # split in python [beginning_of_split:end_of_split]

    return int(first_half, 16)          # converts hexadecimal number to decimal number and returns

def get_h2(sha_string):                 # take second half of sha string and return as integer. usage: get_h2(sha_string)
    midpoint = len(sha_string) // 2
    last_half = sha_string[midpoint:]

    return int(last_half, 16)           # converts hexadecimal number to decimal number and returns

def sizeFilter(n, p):                   # calculate m = number of bits in array, k = number of hash functions and return. usage: sizeFilter(number of items to insert, false positive rate)
    m = math.ceil((-n * math.log(p)) / (math.log(2) ** 2))
    k = math.ceil((m/n) * math.log(2))
    return m, k

def main():
    n = totalItems
    p = falsePositiveRate
    m, k = sizeFilter(n, p)

    print(f"Total items to be inserted: {n}\nFalse Positive Rate = {p}\nNumber of bits in array: {m}\nNumber of hash functions: {k}")

if __name__ == "__main__":
    main()
