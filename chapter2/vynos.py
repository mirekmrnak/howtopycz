"""
Vzorec pro výpočet výsledné hodnoty A počátečního vkladu P

A = P ( 1 + r/n) ** n.t

P = počáteční vklad
r = úroková míra per annum jako desetinné číslo
n = počet hodnocených období za rok
t = počet roků
Pro P=10000 Kč, n=12 měsíců, r=8%(0,08) a t=10 let by hodnota A měla být přibližně 22196.4 Kč
"""

def vynos(P, r, t, n=12):
    vynos = (P * (1 + r / n) ** (n*t))
    return f'Výnos z vkladu {P}Kč za {t} let při úrokové sazbě {r*100}% je {vynos:.2f}Kč'

print(vynos(10000, 0.08, 10))