inpath = 'files_txt/alice_wonderland.txt'  # cesta k souboru
infile = open(inpath, encoding="utf-8") 
text = infile.read()          # 'text' má formát řetězce
infile.close()

sett = set()              # prázdný kolektor typu 'set'
lstt = text.split()       # konverze stringu na list

for i in lstt:
    sett.add((i, lstt.count(i)))  # 'add' přijímá 1 arg.

lstt_words = (dict(sett))
lstt_sorted = dict(sorted(lstt_words.items(),
                            key=lambda item: item[1],
                            reverse=True))

outpath = 'files_dat/word_counts.dat'   # deklarace cesty
outfile = open(outpath, 'w')      # otevření/vytvoření souboru

# formátované záhlaví souboru:

outfile.write(f"{'Character':12}{'Count'}\n")
outfile.write("=================\n\n")

# formátovaný obsah pod záhlavím:
for word, value in lstt_sorted.items():
    outfile.write(f'{word:12}:{value:>4}x\n')

outfile.close()         # povinné zavření otevřeného souboru