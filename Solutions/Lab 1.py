b = 0
sum = 0
x = 0
while True:
    b = int(input())
    if b > 0:
        if b % 2 == 0 and b != 2:
            b += 0
        elif b == 1:
            b += 0
        elif b == 2:
            sum += b
        elif b % 2 != 0 and b > 2:
            for x in range(2, b):
                if b % x != 0 and x < b-1:
                    sum += 0
                if b % x != 0 and x == b-1:
                    sum += b
                    break
                if b % x == 0:
                    break

    else:
        break
print(sum)