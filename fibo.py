def fibo(n,lookup):
    if n<=1:
        lookup[n]=n


    if lookup[n] is None:
        lookup[n] = fibo(n-1,lookup) + fibo(n-2,lookup)

    return lookup[n]


def main():
    n=34
    lookup = [None]*101
    print("Fibonacci Number is ",fibo(n,lookup))


if __name__ == "__main__":
    main()
    
    
        
