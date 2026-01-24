
index: int = 1
max_rate: int = 0
min_rate: int = 6

while index <= 10:
    print("What is the rate to the movie number ", index)
    rate = int(input())
    if 1 <= rate <= 5:
        index += 1

        if rate > max_rate:
            max_rate = rate

        if rate < min_rate:
            min_rate = rate

    else:
        print("Invalid input")


print("the highest rate is ", max_rate)
print("the lowest rate is ", min_rate)
