def find_outlier(integers):
    odds = []
    evens = []

    for num in integers:
        if (num % 2 == 0):
            evens.append(num)

        elif (num % 2 == 1):
            odds.append(num)

        if (len(evens) > 1 and len(odds) == 1):
            return odds[0]
        if (len(odds) > 1 and len(evens) == 1):
            return evens[0]
