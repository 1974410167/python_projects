import time


list = [
  (1, 2),
  (2, 3),
  (2, 4),
  (3, 5),
  (4, 5)
]

dict_2 = {}
dict_1 = {}

for i in list:

    if i[1] not in dict_1:
        dict_1[i[1]] = 1
    else:
        dict_1[i[1]] += 1

    if i[0] not in dict_2:
        dict_2[i[0]] = [i[1]]
    else:
        dict_2[i[0]].append(i[1])

print(f"dict_1:{dict_1}")
print(f"dict_2:{dict_2}")
head = 0
for j in list:
    if j[0] not in dict_1:
        head = j[0]

res = []
print(f"head:{head}")
while True:

    if head in dict_2:

        while dict_2[head]:
            res.append(head)
            head = dict_2[head].pop()

            if dict_1[head] > 0:
                dict_1[head] -= 1

    print(res)
    print(head)
    print(dict_1)
    print(dict_2)
    time.sleep(1)

