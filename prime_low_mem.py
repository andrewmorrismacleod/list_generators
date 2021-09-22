import math


#Prime sieve
#This is a slightly optimised version of the sieve of Eratosthenes which saves on memory by removing the need
#to compute the n=2 and n=3 loops of the sieve.

def generate_primes(n):

    bound = int((n+2)/3)
    sieve = [False]*bound
    climit = int((int(math.sqrt(n))-1)/2)

    for i in range(2,climit):

        #For each number there are two loops to check

        fi = 3*i-1-(i%2)

        start1 = 2*fi+i
        start2 = 2*fi-(i-1)

        for j in range(start1,bound,2*fi):
            sieve[j] = True

        for j in range(start2,bound,2*fi):
            sieve[j] = True
            
    primes = [2,3]   
    for i in range(2,len(sieve)):
        if not sieve[i]:
            primes.append(3*i-1-i%2)    

    return primes


