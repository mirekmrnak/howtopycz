# countLetters.py

def display(i):  
    '''
    Ošetření tisknutelných (chr(i)) i netisknutelných znaků.
    Tato funkce bude opakovaně použita v následné smyčce.
    Argument 'i' je UCP (Unicode Code Point) zkoumaného znaku.
    '''                                 
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE'
    return chr(i)           # vrací tisknutelný znak.
		
# Načtení textu ze souboru do paměti interpreta: 

inpath = 'files_txt/alice_wonderland.txt'  # cesta k souboru
infile = open(inpath, encoding="utf-8") 
text = infile.read()          # 'text' má formát řetězce
infile.close()

'''
Pro anglický text (kódování ASCII) lze zadat délku seznamu  
counts = 127 * [0], 
pro český text (UTF-8) je nutné zadat counts = 383 * [0]

Případně pokud umíme určit max UCP jako zde:
>>> text = "abcde\n efgh" 
>>> ord(max(text)) --> 104 --> counts = 105 * [0]
můžeme použít seznam kratší.

Položky seznamu 'counts' jsou receptory výskytů jednotlivých 
písmen. Zjištěné hodnoty UCP slouží jako indexy seznamu
'''

# Načtení výskytů do seznamu 'counts':

counts = 127 * [0]                # max UCP pro ASCII = 126
for letter in text:         
    counts[ord(letter)] += 1      # přičítá výskyty znaků
	 # ord(letter) je aktuální index seznamu 'counts'
	                              
# Strukturovaný zápis výskytů do souboru 'letter_counts.dat': 

outpath = 'files_dat/letter_counts.dat'   # deklarace cesty
outfile = open(outpath, 'w')      # otevření/vytvoření souboru

# formátované záhlaví souboru:
outfile.write("%-12s%s\n" % ("Character", "Count"))
outfile.write("=================\n")

# formátovaný obsah pod záhlavím:
for i in range(len(counts)):           # len(counts) = 126+1
    if counts[i]:                        # if counts[i] != 0
        outfile.write("%-12s%d\n" % (display(i), counts[i]))

outfile.close()         # povinné zavření otevřeného souboru

'''
Funkce 'range' v proceduře 'range(len(counts))' 
je důvodem ke zvýšení délky seznmu 'count' o 1.
'''

# Toto oznámení se vytiskne v konzole interpreta IDLE:

print("Frekvenční tabulka je v souboru ", outpath)
print("Délka souboru 'counts' a počet znaků: ", 
                           len(counts), len(text))

# Frekvenční tabulku si prohlédneme v souboru 'letter_counts.dat'.