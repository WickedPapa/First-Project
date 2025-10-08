import statistics
from math import sqrt

altezze = [170, 180, 190]

media = statistics.mean(altezze)
print("media", media)

print("")
# VARIANZA:
# -misura della dispersione dei dati rispetto alla media
# -media delle differenze tra la media e i singoli valori
# -se la varianza è bassa i valori sono concentrati vicino alla media
# -se la varianza è alta i valori sono molto dispersi rispetto alla media

differenza_dalla_media_al_quadrato_valore_1 = (170-180)**2 #100
differenza_dalla_media_al_quadrato_valore_2 = (180-180)**2 #0
differenza_dalla_media_al_quadrato_valore_3 = (190-180)**2 #100
differenze = [
    differenza_dalla_media_al_quadrato_valore_1,
    differenza_dalla_media_al_quadrato_valore_2,
    differenza_dalla_media_al_quadrato_valore_3
]

varianza = statistics.mean(differenze)
print("varianza", varianza)

# DEVIAZIONE STANDARD:
# -radice quadrata della varianza
# -indica quanto i dati si discostano in media dalla media stessa

deviazione_standard = sqrt(varianza)
print("deviazione_standard", deviazione_standard)

###################################################################

print("")
# possiamo calcolare varianza e deviazione standard in modo semplice con la lib statistics
# ATTENZIONE! i metod variance e stdev di statistics usa varianza campione non varianza popolazione.
# (ovvero quando calcola la media non divide per il numero di elementi (in questo caso 3)
# ma per il numero di elementi - 1 (in questo caso 2)

variance = statistics.variance(altezze)
print("sample variance", variance)

standard_deviation = statistics.stdev(altezze)
print("standard deviation from sample variance", standard_deviation)

###################################################################

print("")
# per usare varianza popolazione esistono i metodi pvariance e pstdev
pvariance = statistics.pvariance(altezze)
print("population variance", pvariance)

p_standard_deviation = statistics.pstdev(altezze)
print("standard deviation from population variance", p_standard_deviation)