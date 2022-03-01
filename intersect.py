def intersect (set1, set2):
    intersec = set()
    for num1 in set1:
            for num2 in set2:
                if num1 == num2:
                    intersec.add(num1)
    print(intersec)