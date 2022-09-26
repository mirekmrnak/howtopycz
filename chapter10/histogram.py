import random

def gen_number(min, max):
    #return random.randrange(min, max)
    return random.randint(min, max)

def randomList(n):    
    s = [0] * n                    # počáteční seznam s nulami
    for i in range(n):             # náhrada nul za náhodné číslo
        s[i] = random.random()
    return s                       # seznam 'n' náhodných čísel

def inBucket(list, low, high):
    count = 0
    for num in list:
        if low <= num < high:
            count = count + 1
    return count

def buckets_a(n, b):
    výskyty = [0] * b                    # počáteční seznam s nulami
    bucketWidth = max(n) / b             # číselný rozsah jednoho intervalu
    for i in range(b):                   # pro každý kyblík určit:
        low = i * bucketWidth            # dolní mez intervalu
        high = low + bucketWidth         # horní mez intervalu
        výskyty[i] = inBucket(n, low, high)    # viz **
    return (výskyty)     # ** náhrada nul počtem příslušných náhodných čísel

def buckets_b(list, b):
    výskyty = [0] * b           # akumulátor
    for i in list:
        index = int(i * b)      # zaokrouhlení dolů          
        výskyty[index] = výskyty[index] + 1
    return (výskyty)

a = randomList(8000)
print(sum(buckets_a(a, 8)), buckets_a(a, 8))
print(sum(buckets_b(a, 8)), buckets_b(a, 8))
