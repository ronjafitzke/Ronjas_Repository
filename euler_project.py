def problem_1():
    sum = 0
    for i in range(3, 1000, 3):
        sum += i
    for j in range(5, 1000, 5):
        if j % 3 != 0:
            sum += j

    print(sum)
    return sum

problem_1()


def problem_2():
    a = 0
    b = 1
    even_sum = 0

    while b <= 4000000:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    print(even_sum)
    return even_sum

problem_2()


def problem_3(n):
    prime_factor = 1
    i = 2

    while i <= n:
        if n % i == 0:
            prime_factor = i
            n //= i
        else:
            i += 1

    print(prime_factor)
    return prime_factor


problem_3(600851475143)


def problem_4():
    zahl = max(i * j
               for i in range(100, 1000)
               for j in range(100, 1000)
               if str(i * j) == str(i * j)[:: -1])
    print(zahl)
    return zahl

problem_4()
