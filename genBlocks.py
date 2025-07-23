def blocks():
    array = []
    for i in range(0, 1900, 50):
        array.append([i, 800])
    for i in range(600, 1900, 50):
        array.append([i, 450])
    for i in range(50, 900, 50):
        array.append([i, -100])
    for i in range(-9200, 800, 50):
        array.append([0, i])
        array.append([1850, i])
    array.append([400, 750])
    return(array)
def blocks2():
    array = [[], []]
    for i in range(0, 1900, 50):
        array[0].append([i, 0])
    for i in range(600, 1900, 50):
        array[0].append([i, 350])
    for i in range(50, 900, 50):
        array[0].append([i, 900])
    for i in range(0, 10000, 50):
        array[0].append([0, i])
        array[0].append([1850, i])
    array[0].append([400, 50])
    for i in range(50, 950, 50):
        if 450<i<850:
            array[0].append([i, 1350])
            array[1].append([i, 1400])
        else:
            array[0].append([i, 1400])
    array[0].append([50, 1700])
    array[0].append([400, 2150])
    array[0].append([450, 2150])
    for i in range(800, 1900, 50):
        array[0].append([i, 2700])
    array[0].append([800, 3000])
    array[0].append([850, 3000])
    array[0].append([1000, 3000])
    array[0].append([1050, 3000])
    for i in range(0, 750, 50):
        array[0].append([i, 3500])
    for i in range(1150, 1900, 50):
        array[0].append([i, 3500])
    for i in range(850, 1050, 50):
        array[0].append([i, 4000])
    array[1].append([850, 4050])
    array[1].append([1000, 4050])
    for i in range(3050, 4100, 50):
        if i > 3800  or i < 3600:
            array[1].append([800, i])
            array[1].append([1050, i])
    for i in range(0, 750, 50):
        array[0].append([i, 4500])
    for i in range(1150, 1900, 50):
        array[0].append([i, 4500])
    array[0].append([50, 5000])
    array[0].append([350, 5500])
    array[0].append([650, 6000])
    array[0].append([950, 6500])
    array[0].append([1250, 7000])
    array[0].append([1550, 7500])
    array[0].append([1700, 8000])
    for i in range(50, 1750, 50):
        array[0].append([i, 8300])
        if i%3 ==0:
            for j in range(8350, 8800, 50):
                array[1].append([i, j])
        else:
            array[0].append([i, 8350])
    for item1 in array:
        for item2 in item1:
            item2[1] = 800-item2[1]
    return(array)
