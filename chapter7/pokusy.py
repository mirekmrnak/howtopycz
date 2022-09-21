#otevirani s open
file = open("chapter7/data.txt", "r")
print(file.readlines())
file.close()

#otevirani s 'with' --> soubor automaticky zavre
with open("chapter7/data.txt", "r") as file:
    print(file.readlines())

# copy-easter.py
f = open("chapter7/easter_328kb.jpg", "rb")   # existující kopírovaný soubor
g = open("chapter7/easter_copy.jpg", "wb")    # nový (prázdný) soubor tamtéž

while True:
    buff = f.read(3300)              # pomocný objekt 3300 bitů
    if len(buff) == 0:
         break
    g.write(buff)

f.close(); g.close()	