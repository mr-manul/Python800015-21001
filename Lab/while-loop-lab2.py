sum = 0

count = 1
while count >= 100 :
    if count % 3 == 0:
        sum = sum + count
        count += 1

print(sum)