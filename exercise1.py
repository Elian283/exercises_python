def cagr_berechnung(AK, EK, t):
    AK=abs(AK)
    t= abs(t)
    cagr = (EK/AK)**(1/t)-1
    return cagr

x=cagr_berechnung(100,700, 30)

print(x*100)

AK=120
t=30
EK_2=AK*(1+x)**t

print(EK_2)


    