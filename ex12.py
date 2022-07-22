sum = 0
no = 1

while no <= 10:
    sum += no
    no += 1

print(sum)


print("====================================")

num = 0

while True:
    num += 1
    if num%6==0 and num%14==0:
        print(num)
        break