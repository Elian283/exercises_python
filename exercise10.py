import numpy as np

# Erstellen Sie ein 2D-Array mit zehn Zeilen, wobei jede Zeile von 1 bis 10 geht
D = np.tile(np.arange(1, 11), (10, 1))

# Berechnen Sie die Summe über die Zeilen
summe_zeilen = np.sum(D, axis=0)

# Berechnen Sie den Mittelwert über die Spalten
mittelwert_spalten = np.mean(D, axis=1)

# Ausgabe der Ergebnisse
print("2D-Array D:")
print(D)
print("Summe über die Zeilen:")
print(summe_zeilen)
print("Mittelwert über die Spalten:")
print(mittelwert_spalten)
