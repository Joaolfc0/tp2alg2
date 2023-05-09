class TrieNode:
    def __init__(self):
        self.filho = {}
        self.index = -1

class Trie:
    def __init__(self):
        self.raiz = TrieNode()
        self.index = 0

    def insert(self, palavra):
        node = self.raiz
        for c in palavra:
            if c not in node.filho:
                node.filho[c] = TrieNode()
            node = node.filho[c]
        node.index = self.index
        self.index += 1

    def search(self, palavra):
        node = self.raiz
        for c in palavra:
            if c not in node.filho:
                return -1 
            node = node.filho[c]
        return node.index

    def search_output(self, palavra):
      node = self.raiz
      for c in palavra:
        if c not in node.filho:
            return node.index
        node = node.filho[c]
      return node.index

    