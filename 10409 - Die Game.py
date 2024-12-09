while True:
    try:
        n = int(input())
        if n == 0:
            break
        codes = [input() for _ in range(n)]
        north, west, top = 2, 3, 1
        for code in codes:
            if code == 'east':
                north, west, top = north, 7 - top, west
            elif code == 'south':
                north, west, top = 7 - top, west, north
            elif code == 'west':
                north, west, top = north, top, 7 - west
            elif code == 'north':
                north, west, top = top, west, 7 - north        
        print(top)
    except EOFError:
        break