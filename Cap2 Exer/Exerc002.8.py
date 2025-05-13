'''Em que ordem os operadores nas expressões a seguir são avaliados?


2 + 3 == 4 or a >= 5
lst[1] * -3 < -10 == 0
(lst[1] * -3 < -10) in [0, True]
2 * 3**2
4 / 2 in [1, 2, 3]
'''

list = [3,5,6,5,9,4,6,7,9,8]
mediaList = sum(list) / len(list)
list.remove(5)
list.append(5)
list.reverse()
list.count(6)
list.index(3)
list.sort()
list.pop()
list.insert(2, 8)

print(mediaList)
x = 3 in list
print(x)
print(list)