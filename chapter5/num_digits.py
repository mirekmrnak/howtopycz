def num_digits(n):
    if n == 0: return 1     # specielní případ
    elif n < 0: n = abs(n)
    
    count = 0               # počítadlo	
    while n:            
        count += 1         
        n = n//10           # celočíselné dělení
    return count

print(num_digits(-4656))