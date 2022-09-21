import mymodule1
import mymodule2

print((mymodule1.myage - mymodule2.myage)
                == (mymodule1.year - mymodule2.year))

s = "If we took the bones out, \ it wouldn't be crunchy, would it?"
print(s.split())
print('0'.join(s.split('o')))