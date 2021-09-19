from itertools import count, cycle

def generate_infinite_list(start, max):
    for item in count(start=start, step=1):
        if item>max: 
            break 
        yield item

def generate_cycle_list(repo, cycle_number):
    index_cycle = 0
    for item in cycle(repo):
        if index_cycle==cycle_number*len(repo): 
            break
        index_cycle +=1
        yield item

def main():
    for item in generate_infinite_list(5, 10):
        print(item)
    for item in generate_cycle_list(['first', 'second', 'third', '---'], 3):
        print(item)

if __name__=='__main__':
    main()