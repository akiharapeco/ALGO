from typing import List

class Node:
    child = {} 
    def setChild(self, c):
        if not self.child.haskey(c):
            self.child[c] = {}
        
class Trie:
    head = Node
    def search(self, string):
        node = self.head.child
        for c in string:
            if c not in node:
                return False
            node = node[c]
        if None in node:
            return False
        return True
    
    def insert(self, string):
        node = self.head.child
        for c in string:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[None] = None

from collections import defaultdict
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #trie = Trie()
        #for word in wordDict:
        #    trie.insert(word)
        cache = {}
        def backtracking(s):
            if s in cache:
                return cache[s]
            if not s:
                return True
            res = False
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    res |= backtracking(s[i:]) 
            cache[s] = res
            return res
        
        return backtracking(s)