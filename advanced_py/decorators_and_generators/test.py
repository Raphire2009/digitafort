def get_number_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
        print(result[0])
    return result 

#num = get_number_list(1_000_000)
#rint(num)


def get_number2(n):
    for i in range(n):
        yield i * i


#num = get_number2(1_000_000)
#print(next(num))
#print(next(num))
#print(next(num))



def countdown(n):
    print("Starting countdown...")
    while n > 0:
        yield n
        n -= 1
    print("Done!")

gen = countdown(5)
print(next(gen))
print(next(gen))
print(next(gen))
