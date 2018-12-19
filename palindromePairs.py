from collections import defaultdict

def isPalindrome(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and isPalindrome(word[1:-1])

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        '''
        The trie has a next which goes to the next char.
        The end trie is such that it holds not char, just that it is a left and the index.
        palindromesBelow tells is for a certain node, what indicies are below it such that the parts below of these indicies are palindromes. 
        For example if we have a word abcdc with index 5 the node with b in it will have palindromesBelow having 5 in it and the node after c will be just having index = 5 in it, and empty other fields. 
        '''
        
        class Trie(object):
        
            def __init__(self):
                self.next = defaultdict(Trie)
                self.index = -1
                self.palindromesBelow = []
                
            def addWord(self, word, index):
                
                trie = self
                
                for i,c in enumerate(reversed(word)):
                    if isPalindrome(word[0:len(word)-i]):
                        trie.palindromesBelow.append(index)
                    trie = trie.next[c]
                trie.index = index
        
        pairs = []
        
        trie = Trie()
        for index, word in enumerate(words):
            trie.addWord(word, index)
        
        def getCandidates(trie, word, index):
            candidates = []
            
            while word:
                
                # Palindrome of the form A B where |A| > |B|.
                if trie.index >= 0:
                    if isPalindrome(word):
                        candidates.append(trie.index)
                # The trie ended. Either this node will be the end of some reversed word.
                if word[0] not in trie.next:
                    return candidates
                else:
                    trie = trie.next[word[0]]
                    
                word = word[1:]

            # Here, the trie has been traversed fully.
            
            # Palindrome A B where |A| = |B|. 
            if trie.index >= 0:
                candidates.append(trie.index)
                
            # Palindrome A B where |B| > |A|.
            candidates.extend(trie.palindromesBelow)
            
            return candidates
        
        output = []
        for i, word in enumerate(words):
            candidates = getCandidates(trie, word, i)
            output.extend([[i, c] for c in candidates if i != c])
        return output
                
                    
                    
                    
                    
                    
            
            
        
        
                
                    
                
            
