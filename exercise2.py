def teilbarkeit_pruefen(x, y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen!")
    elif x % y == 0:
        print("x ist durch y teilbar.")
    else:
        print(" x ist nicht durch y teilbar.")
    if x == y:
        print("x und y sind gleich")

x = 12
y = 0
teilbarkeit_pruefen(x, y)

