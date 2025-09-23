set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {1,2,3,4,5,6,7,8,9,10, 10, 10, 10, 1, 2 , 5, 2}
print(set1)
print(set2)

#posso usare anche il costruttore set che vuole un iterabile, utile per rimuovere duplicati
list_1 = [1,2,3,4,5,6,7,8,9,10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1)
set_from_list = set(list_1)
print(set_from_list)

#metodi utili
set_3 = {1,2,3,4,5,6,7,8,9,10}
set_3.add(11)
set_3.discard(11)
set_3.discard(214) #non da errore
#set_3.remove(12414) errore!
print(set_3.pop()) #estrae il primo inserito

#i set usano anche le operazioni insiemistiche:
#UNIONE, INTERSEZIONE, DIFFERENZA, DIFFERENZA SIMMMETRICA

a = {1,2}
b = {2,3}
print("a: ", a)
print("b: ", b)
#UNIONE ritorna i due set uniti senza duplicati

print("UNIONE")
c = a | b
d = a.union(b)
e = b.union(a)
print("c: ",c,"d: ",d,"e: ", e)

print("INTERSEZIONE")
c = a & b
d = a.intersection(b)
e = b.intersection(a)
print("c: ",c,"d: ",d,"e: ", e)

print("DIFFERENZA")
c = a - b
d = a.difference(b)
e = b.difference(a)
print("c: ",c,"d: ",d,"e: ", e)

print("DIFFERENZA SIMMETRICA")
c = a ^ b
d = a.symmetric_difference(b)
e = b.symmetric_difference(a)
print("c: ",c,"d: ",d,"e: ", e)

#esistono anche issubset(), issuperset() e isdisjoint()