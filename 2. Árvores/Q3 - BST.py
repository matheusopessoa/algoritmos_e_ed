class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.level = 0  # o nivel comeca em 0


class BinaryTree:
    def __init__(self):
        self.root = None

    def _search(self, root, key, level): #serve para saber o level_before de um node que foi busccado
        if root.key: 

            if root.key == key:
                return root, level
            elif key < root.key:
                root.left, level_before = self._search(root.left, key, level + 1)
                return root, level_before
            else:
                root.right, level_before = self._search(root.right, key, level + 1)
                return root, level_before
        
        return False, False 

    def find_node(self, key, node): #como tem o and que verifice se existe nó filho no lado desejado,
                                    #é impossivel buscar nó inexistente; -retorna True ou None-
        if key < node.key and node.left:
            return self.find_node(key, node.left)
        elif key > node.key and node.right:
            return self.find_node(key, node.right)
        elif key == node.key: 
            return True

    def insert(self, key):
        self.root = self._insert(self.root, key, 0)

    def _insert(self, root, key, level):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key, level + 1)
        elif key > root.key:
            root.right = self._insert(root.right, key, level + 1)
        return root

    def move_to_root(self, key, action): #A raíz que ele recebe é a do INPUT!
                                         #Verifica existencia/nível e faz os prints
        if self.find_node(key, self.root):
            level_before = self._search(self.root, key, 0) 
            self.root = self._move_to_root(self.root, key, action) 
            print(f'{level_before}')
        else:
            print('-1')

    def _move_to_root(self, root, key, action): #literalmente apenas move pro topo (mantendo a BT)
        if key < root.key:
            root.left = self._move_to_root(root.left, key + 1, action)
            if action == 'SCH':  # so faz a rotacao se for o caso de uma busca
                root = self.rotate_right(root)
        else:
            root.right = self._move_to_root(root.right, key + 1, action)
            if action == 'SCH':  # so faz a rotacao se for o caso de uma busca
                root = self.rotate_left(root)
        return root

    def rotate_right(self, node_y):
        node_x = node_y.left
        if node_x:
            right_subtree = node_x.right

            node_x.right = node_y
            node_y.left = right_subtree

            return node_x

    def rotate_left(self, node_x):
        node_y = node_x.right
        if node_y:
            left_subtree = node_y.left

            node_y.left = node_x
            node_x.right = left_subtree

            return node_y

    def process_command(self, command):
        parts = command.split()
        if len(parts) != 2:
            return None

        operation, number_str = parts
        number_int = int(number_str)

        if operation == 'ADD':
            self.insert(number_int)
            self.move_to_root(number_int, operation)  # nesse caso, operation = 'ADD', move to root vai
                                                      # apenas printar o nivel
        elif operation == 'SCH':
            self.move_to_root(number_int, operation)  # printa nivel e faz as rotacoes e manda pra raiz


bst = BinaryTree()
command = 'init'
while command != '':
    try:
        command = input('')
        bst.process_command(command)
    except:
        break

    