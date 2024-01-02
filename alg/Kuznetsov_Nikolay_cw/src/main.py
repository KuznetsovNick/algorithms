from test_avl_tree import TestAVL
from test_hash_table import TestHashTable
from modules.commands import Commands
from modules.hash_table import HashTable
from modules.avl_tree import AVLTree


def breadth_first_search(root, dot):
    queue = [root]
    dot.node(str(root.key))
    while queue:
        tmp_queue = []
        for element in queue:
            if element.left:
                dot.node(str(element.left.key))
                dot.edge(str(element.key), str(element.left.key))
                tmp_queue.append(element.left)
            if element.right:
                dot.node(str(element.right.key))
                dot.edge(str(element.key), str(element.right.key))
                tmp_queue.append(element.right)
        queue = tmp_queue


def main():
    # FOR EXAMPLE
    h = HashTable()
    h.insert(10, "lol")
    h.print()
    test = TestHashTable(1000, Commands.INS)
    test.start()
    test = TestAVL(500, Commands.INS)
    test.start()


if __name__ == "__main__":
    main()
