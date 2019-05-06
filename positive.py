# Request positive integer.
def main():
    num = get_positive_int("Positive integer: ")
    print(num)

def get_positive_int(prompt):
    """ Recursively request for a positive integer """
    while True:
        n = int(input(prompt), 10)
        if n > 0:
            break
        
    return n

if __name__ == "__main__":
    main()