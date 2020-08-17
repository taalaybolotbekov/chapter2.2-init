with open('text.txt') as f:
    a = f.read().split(',')
    print(max(a, key=len))