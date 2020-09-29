def get_list(repo = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]):
    return [item for item in repo if repo.count(item)==1]

def main():
    print(get_list())

if __name__=='__main__':
    main()