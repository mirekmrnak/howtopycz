car = {"brand": "Ford", "model": "Mustang","year": 1964}

print(car.values())
print(dct_range := {x: x**2 for x in range(5)})

keys = ['a', 'b', 'c']
vals = [1, 2, 3]
print({keys:vals for (keys,vals) in zip(keys, vals)})

def func_a(): print("fce-a")
def func_b(): print("fce-b")
def func_c(): print("fce-c")

oslík = {"a": func_a, "b": func_b, "c": func_c}

def print_f(value):              # Včetně částečného ošetření výjimek
	oslík.get(value, lambda: print("Neplatné!"))()

print_f('5')

word_set = {('this', 11), ('at', 9), ('here', 5), ('why', 12), ('is', 2)}
print(type(word_set))
word_dict = dict(word_set)
print(word_dict)
sorted_dict = dict(sorted(word_dict.items(),
                            key=lambda item: item[1],
                            reverse=True))
for i, value in sorted_dict.items():
    print(f'{i} : {value}')

print(f"{'Character':12}{'Count'}")
print("=================\n")