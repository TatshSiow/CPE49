while True:
    try:
        n = list(map(int, input().split()))
    except EOFError:
        break
    
    array = [0] * (n[0])
    
    for i in range(1, n[0]):
        m = abs(n[i+1] - n[i])
        if 0 < m < n[0] and array[m] == 0:
            array[m] = 1
    if sum(array) == n[0] - 1:
        print("Jolly")
    else:
        print("Not jolly")