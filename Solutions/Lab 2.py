inputs = map(str, input().split())
sum_of_int=0
sum_of_float=0.0
concat_of_str=""
for item in inputs:
    if "." in item:
        sum_of_float+=float(item)
    else:
        for chr in item:
            if not 48<=ord(chr)<=57:
                concat_of_str+=item
            else:
                sum_of_int+=int(item)

print(sum_of_float)
print(sum_of_int)
print(concat_of_str)