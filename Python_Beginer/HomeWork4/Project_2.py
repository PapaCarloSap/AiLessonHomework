def get_max_list(data):
    return [data[index] for index in range(len(data)) if index != 0 and data[index-1]<data[index] ]

def main():
    print(get_max_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))

if __name__=='__main__':
    main()