import math

# Global variables --------------------------------------------------------

totalItems = 900000
falsePositiveRate = 0.01

# -------------------------------------------------------------------------

def sizeFilter(n, p):
    m = math.ceil( (-n * math.log(p)) / (math.log(2) ** 2))
    k = math.ceil( (m/n) * math.log(2))
    return m, k

def main():
    n = totalItems
    p = falsePositiveRate
    m, k = sizeFilter(n, p)
    print(f"Total items to be inserted: {n}\nFalse Positive Rate = {p}\nNumber of bits in array: {m}\nNumber of hash functions: {k}")


if __name__ == "__main__":
    main()
