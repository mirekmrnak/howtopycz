def print_multiplies(n):
    #nasobilka do n
    for i in range(1, n+1):
        print(n*i, '\t', end="")
    print()

for i in range(11):
    print_multiplies(i)
