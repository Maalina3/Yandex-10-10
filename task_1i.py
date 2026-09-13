import sys


def main():
    
    def power(a, n):
        if n < 0:
            return 1 / power(a, n)
        if n == 0:
            return 1
        if n == 1:
            return a
        if n % 2 == 0:
            return power(a*a, n//2)
        else:
            return a * power(a, n - 1)
    print(power(float(input()), float(input())))

if __name__ == '__main__':
    main()