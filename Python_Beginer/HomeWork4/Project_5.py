from functools import reduce

def get_list(repo = range(100,1001)):
    return reduce(lambda a,b: a*b, ([item for item in repo if item%2==0]))

def main():
    print(get_list())

if __name__=='__main__':
    main()