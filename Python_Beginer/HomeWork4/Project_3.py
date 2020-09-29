def find_multiple(collection = range(20, 240), num_1=20, num_2=21):
    return [item for item in collection if item%num_1==0 or item%num_2==0 ]

def main():
    print(find_multiple())

if __name__=='__main__':
    main()
