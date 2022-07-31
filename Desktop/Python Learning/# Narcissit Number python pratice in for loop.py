# Narcissit Number python pratice in for loop


print("all Narcissit Number between 1000 to 1000")
for i in range(100,1000):
    # hundreds digits 123//100 =1
    x = i // 100
    # ten digit 123//10=12 12%10=2
    y = i // 10 % 10
    # digit 123 % 10  = 3
    z = i % 10
    if x ** 3 + y ** 3 + z ** 3 == i:
        print("i="+str(i))
