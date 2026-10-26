n = input("Введите число N: ")

if not n.isdigit() or int(n) < 2:
    print("Ошибка! Введите целое число не меньше 2.")
else:
    n = int(n)
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    for i in range(2, n + 1):
        if prime[i]:
            print(i)