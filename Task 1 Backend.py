#Task 1 (Backend) : Check Prime Numbers and Represent in Binary

start = int(input("Enter your start number (inclusive): "))
end = int(input("Enter your stop number (exclusive): "))
a = {}
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
def isPrime(n):
    d = get_divisors(n)
    if (d==[1,n]):
        #print("Is prime,",d)
        a[n] = (bin(n))[2:]
    else:
        #print("Is not prime,",d)
        a[n] = d

for i in range(start,end):
    isPrime(i)
print("\nPrime number dictionary: \n",a)
