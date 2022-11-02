# odd number ==> after dividing by 2,the number reminder will be 1
# even number ==> after dividing by 2, the reminder will be 0

num =7
# print(7/2)
# print(7%2)
# print(8%2)
while num <= 20:
    num = num + 1
    if num % 2 == 1:
        continue
    print(num)