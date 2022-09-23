def truth_table(expression): 
    print(f" p      q     {expression}")
    delka = len(f" p      q     {expression}")
    print(delka* "=")

    for p in True, False:
        for q in True, False:
            print(f"{p:<7} {q:<7} {eval(expression):<7}")
    print()

expressions = [
    'p or q',
    'p and q',
    'not (p or q)',
    'not (p and q)',
    'not(p) or not(q)',
    'not(p) and not(q)',
]

for expression in expressions:
    truth_table(expression)

  