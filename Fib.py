
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    


for i in range(1,7):
    print(i,"+",fibonacci(i))

    




cache= {}

value = 0
def fibonacci2(n):

    if n in cache:
        return cache[n]

    if n ==1:
        value = 1
    elif n ==2:
        value = 1
    elif n>2:
        value =fibonacci2(n-1)+ fibonacci2(n-2)
    
    cache[n] =value
    return value

for i in range(1,11):
    print(i,"+",fibonacci(i))







from functools import lru_cache
@lru_cache (maxsize=10000)
def fibonacci3(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return fibonacci3(n-1)+ fibonacci3(n-2)

for i in range(1,1000):
     print(f"{i} Term: {fibonacci3(i)}")



def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print("Move disk 1 from source", source, "to", destination_rod)
        return
    TowerOfHanoi(n-1, source, auxiliary_rod, destination_rod)  # fix: correct rod order
    print("Move disk", n, "from source", source, "to", destination_rod)
    TowerOfHanoi(n-1, auxiliary_rod, destination_rod, source)

n = 3
TowerOfHanoi(n, source='A', destination_rod='C', auxiliary_rod='B')



