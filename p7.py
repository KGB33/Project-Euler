#Project Euler, Problem 7



#success, just took a long time
def primesfxn():
    primes = (2,)
    i = 1
    j = 3
    k = 2
    while k < j and i < 10002:
        if k == j-1:
            primes = primes + (j,)
            k = 2
            j =j + 1
            i = i + 1
        elif j%k==0:
            k=2
            j=j+1
        else:
            k = k+1
    print(primes)



primesfxn()





















# dont know if this method works
def findprimes():
    primes = (2,)
    i = len(primes)
    k = 15
    while i != 10:
        i = len(primes)
        j = 2
        k=k+1
        while j < k:
            if j == k-1 and k%j==0:
                primes = primes + (i,)
                print(j,k,primes)
                j = 2
                k=k+1
                break
            elif k%j==0:
                print(j,k,primes)
                j=j+1
            else:
                j = j+1
                print('miss')
    print(primes)

#findprimes()
