class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return True
        elif node.leaf:
            return False
        else:
            return self._search(node.child[i], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_node = BTreeNode(False)
            self.root = new_node
            new_node.child.insert(0, root)
            self._split_child(new_node, 0)
            self._insert_non_full(new_node, key)
        else:
            self._insert_non_full(root, key)
    
    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.child[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.child[i], key)
    
    def _split_child(self, node, i):
        t = self.t
        child = node.child[i]
        new_child = BTreeNode(child.leaf)
        node.child.insert(i + 1, new_child)
        node.keys.insert(i, child.keys[t - 1])
        new_child.keys = child.keys[t:(2 * t) - 1]
        child.keys = child.keys[0:(t - 1)]
        if not child.leaf:
            new_child.child = child.child[t:(2 * t)]
            child.child = child.child[0:t]

    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    def  search_key(self, k, x = None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])
        else:
            return self.search_key(k, self.root)
        
def main():
    B = BTree(3)

    for i in range(10):
        B.insert((i, 2 * i))

    B.print_tree(B.root)

    if B.search_key(8) is not None:
        print("\nFound")
    else:
        print("\nNot Found")

if __name__ == '__main__':
    main()