def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i +5) + '*' * (2 * i - 1))

inverted_pyramid(int(input( "enter a value: ")))
