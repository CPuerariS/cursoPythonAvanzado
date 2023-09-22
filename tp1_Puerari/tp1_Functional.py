# - Realizar un programa que, a su criterio, es mas adecuado para ser resuelto con programacion funcional.
# - El programa debe tener al menos 3 funciones. Una de cada tipo: map, reduce, filter
#En ambos casos, se requiere una explicacion de porque se eligio esa forma de resolver el problema.
#Dicha explicacion debe estar correctamente documentada (preferentemente a través de un archivo con extensión .md)
from functools import reduce

num = [1,2,3,4,5,6,7,8,9]

mapped_nums = list(map(lambda x: x * 2, num))
print (mapped_nums)

filter_nums = list(filter(lambda x: x % 2 == 0, num))
print (filter_nums)

reduce_nums = reduce(lambda x, y: x + y, num)
print (reduce_nums)
