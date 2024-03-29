N = int(input())

while N:
    F = input().split()
    F.sort()
    F1, F2 = map(int, F)

    # if cards number isn't multiples of each other
    # find the remainder cards number
    # that will be the required stack sizw
    while F1 % F2 != 0:
        temp = F1
        F1 = F2
        F2 = temp % F2

    print("%d" % F2)
    N -= 1
