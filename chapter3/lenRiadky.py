def three_lines():
    print('\n')
    print('\n')
    print('\n')

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def cat_times(s,n):
    print(f'{s*n}')

cat_times('Spam', 5)