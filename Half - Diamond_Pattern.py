
#Half - Diamond Pattern  
'''
Print 

   *
  ***
 *****
*******

'''

def diamondpattern(n):
    # Print the n number of rows
    for i in range(1, n + 1):
        # n - i spaces
        for space in range(0, n - i):
            print(" ", end="")

        # 2*i - 1 stars
        for star in range(0, 2 * i - 1):
            print("*", end="")

        # New line
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    diamondpattern(n)

