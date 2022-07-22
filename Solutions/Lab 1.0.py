a = []
b = int()
sum = 0
while True:
    b = int(input())
    if b > 0:
        a.append(b)
    else:
        break
for c in a:
    if c % 2 == 0 and c != 2:
        a.remove(c)
    if c == 1:
        a.remove(c)
for d in range(2, a[-1]+1):
    for e in range(2, a[-1]+1):
        if d != e:
            if d % e == 0 and d > e:
                if d in a:
                    a.remove(d)
            if e % d == 0 and e > d:
                if e in a:
                    a.remove(e)
for f in a:
    sum += f
print(a)
print(sum)