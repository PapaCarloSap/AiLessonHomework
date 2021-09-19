from itertools import count

def fact(value):
    buffer = 1
    for item in range(1, value+1):
        buffer = buffer*item
        yield buffer


def main():
    for item in fact(10):
        print(item)

if __name__=='__main__':
    main()