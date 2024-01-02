from modules.find_length import find_length
from modules.make_tree import make_tree


def main():
    trash = input()
    parents = [int(x) for x in input().split()]
    leafs, parents = make_tree(parents)
    if len(parents) == 1:
        print(1)
    else:
        print(find_length(leafs, parents))


if __name__ == '__main__':
    main()
