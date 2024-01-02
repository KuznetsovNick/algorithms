from modules.node import Node


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.root:
            self.root = new_node
        else:
            self.root = self.insert_rec(new_node, self.root)

    def insert_rec(self, new_node, node):
        if not node:
            return new_node

        if new_node.key < node.key:
            node.left = self.insert_rec(new_node, node.left)
            if abs(self.get_height(node.left) - self.get_height(node.right)) == 2:
                if new_node.key > node.left.key:
                    node = self.big_right_rotate(node)
                else:  # key < b
                    node = self.small_right_rotate(node)
        elif new_node.key > node.key:
            node.right = self.insert_rec(new_node, node.right)
            if abs(self.get_height(node.right) - self.get_height(node.left)) == 2:
                if new_node.key < node.right.key:
                    node = self.big_left_rotate(node)
                else:  # key > b
                    node = self.small_left_rotate(node)

        elif new_node.key == node.key:
            raise ValueError("Ключ со значением {} уже присутствует".format(new_node.key))

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return node

    def remove(self, elem):
        self.root = self.remove_rec(elem, self.root)

    def remove_rec(self, key, node):
        if node is None:
            raise ValueError("Ключа {} нет в дереве".format(key))

        if key < node.key:
            node.left = self.remove_rec(key, node.left)
            if abs(self.get_height(node.left) - self.get_height(node.right)) == 2:
                if node.right is None:
                    node = self.big_left_rotate(node)
                elif node.right is None:
                    node = self.small_left_rotate(node)
                elif key > node.left.key:
                    node = self.big_right_rotate(node)
                else:
                    node = self.small_right_rotate(node)
        elif key > node.key:
            node.right = self.remove_rec(key, node.right)
            if abs(self.get_height(node.right) - self.get_height(node.left)) == 2:
                if node.right is None:
                    node = self.big_right_rotate(node)
                elif node.left is None:
                    node = self.small_right_rotate(node)
                elif key < node.right.key:
                    node = self.big_left_rotate(node)
                else:
                    node = self.small_left_rotate(node)

        elif node.key == key:  # можно удалить из поддерева большей высоты, чтобы было меньше балансирования
            if node.left and node.right:
                change_elem = self.findMax_rec(node.left)
                node.key = change_elem.key
                node.left = self.remove_rec(node.key, node.left)
            else:
                if node.right:
                    node = node.right
                    return node
                elif node.left:
                    node = node.left
                    return node
                else:
                    node = None
                    return node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self.findMax_rec(self.root)

    def findMax_rec(self, node):
        if node.right:
            return self.findMax_rec(node.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self.findMin_rec(self.root)

    def findMin_rec(self, node):
        if node.left:
            return self.findMin_rec(node.left)
        else:
            return node

    def find(self, key):
        return self.find_rec(key, self.root)

    def find_rec(self, key, node):
        if node is None:
            return None
        if key < node.key:
            return self.find_rec(key, node.left)
        if key > node.key:
            return self.find_rec(key, node.right)
        return node.value

    def get_height(self, node):
        if not node:
            return -1
        else:
            return node.height

    def small_left_rotate(self, node_a):
        node_b = node_a.right
        Lb = node_b.left
        node_a.right = Lb
        node_b.left = node_a

        node_a.height = max(self.get_height(node_a.right), self.get_height(node_a.left)) + 1
        node_b.height = max(self.get_height(node_b.right), self.get_height(node_b.left)) + 1

        return node_b

    def small_right_rotate(self, node_a):
        node_b = node_a.left
        Rb = node_b.right
        node_a.left = Rb
        node_b.right = node_a

        node_a.height = max(self.get_height(node_a.right), self.get_height(node_a.left)) + 1
        node_b.height = max(self.get_height(node_b.right), self.get_height(node_b.left)) + 1

        return node_b

    def big_left_rotate(self, node_a):
        node_a.right = self.small_right_rotate(node_a.right)
        return self.small_left_rotate(node_a)

    def big_right_rotate(self, node_a):
        node_a.left = self.small_left_rotate(node_a.left)
        return self.small_right_rotate(node_a)
