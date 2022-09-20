def print_triangular_numbers(n):
    count = 1
    i = 1
    while count < n:
        print(count, '\t', i)
        count += 1
        i += count

print_triangular_numbers(6)

#1, 2, 3, 6, 10, 15