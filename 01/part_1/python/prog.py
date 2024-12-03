

def extract_lists() -> (list, list):
    filename = 'input.txt'
    
    l1 = []
    l2 = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line[:-1]
            if not line:
                continue
            line = line.split('   ')
            l1.append(int(line[0]))
            l2.append(int(line[1]))
 
    return l1, l2


def distance(a: int, b: int) -> int:
    if a >= b:
        return a - b
    return b - a


def pop_smallest(lst: list[int]) -> int:
    small = lst[0]
    for number in lst:
        if number < small:
            small = number
    lst.remove(small)
    return small


def main():
    l1, l2 = extract_lists()
    
    total = 0
    while l1:
        small1 = pop_smallest(l1)
        small2 = pop_smallest(l2)
        dist = distance(small1, small2)
        total += dist
    
    print("Answer:", total)



if __name__ == '__main__':
    main()



