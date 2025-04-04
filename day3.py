# Searching algorithm

class LinearSearch:

# Unordered linear search
    def unordered_linear_search(A, n, data):
        for i in range(n):
            if A[i] == data:
                return i
        return -1
    
# Ordered linear search
    def ordered_linear_search(A, n, data):
        for i in range(n):
            if A[i] == data:
                return i
            elif A[i] > data:
                #if A[i] is greater than the data searched, jsut return -1 w/o searching the rest
                return -1
            return -1
        
# Binary search (iterative)
    def binary_search_iterative(A, n, data):
        low = 0 #initialized ti first index
        high = n - 1 #last index

        while low <= high: # code continues as long as the low is <= to the high
            mid = low + (high - low) // 2 #Avoid overflow

            if A[mid] == data:
                return mid
            #if middle element is equal to data, the index mid is returned
            elif A[mid] < data:
                low = mid + 1
            #if mid elemnet is less than dta, data must be in the upper half, so low is updated
            else:
                high = mid - 1
            #if mid greater than the data, the data must be in the lower half

        return -1
    #return -1 if loop exists without finding data
    
# Binary search (recursive)
    def binary_search_recursive(A, low, high, data):
        if low > high:
            return -1
        #this checks if search range is valid
        
        mid = low + (high - low) // 2 #avoid overflow

        if A[mid] == data:
            return mid
        
        elif A[mid] < data:
            return binary_search_recursive(A, mid + 1, high, data) # type: ignore
        #if mid is greater, the function calls itself recursivley to serach the upper half
        else:
            return binary_search_recursive(A, low, mid -1, data) # type: ignore


# String Algorithm
class StringAlgorithm:

    def brute_force_match(T, n, P, m):
        # n = length of T, m = length of P
        for i in range(n - m + 1):
            #in range of possible comparisions
            #the loop iterates over T from index 0 to n-m
            #ensuresthere is enough room left in T to match
            j = 0
            #initializes index j to 0
            while j < m and P[j] == T[i + j]:
            #checkes if  chracters in P and T match

                j += 1
                #increments and checkd for next
            if j == m: #if all characters match
                return i
        return -1
    
# Storing strings
class TrieNode:
    def __init__(self, data):
        self.data = data #character stored in node
        self.is_end_of_string = False #indicates wether node makrks end of string
        self.children = [None] * 26 # Array of 26 pointers for 'a' to 'z'

    def search_in_trie(root, word):
        if root is None:
            #if trie is empty it means the search has reached a non-existent mode
            return -1
        #means word cannt be found

        if not word:
            #means empty string is a valid entry in trie and returns 1
            if root.is_end_of_string:
                return 1
            else:
                return -1
            #means string not empty

        if root.data == word[0]:
            #first character matches current data, the func recursively calls itself
            #it moves to the child node correspondind to the first character
            #also passes the rest of the word to the recursive call
            return TrieNode.search_in_trie(root.children[ord(word[0]) - ord('a')], word[1:])
        else:
            return -1    
        #if first charac of the word does not match the node's data, the func return -2, indicating search failed


class TSTNode:
    def __init__(self, data):
        self.data = data #Character
        self.is_end_of_string = False # a boolean which indicates if a node marks the end
        self.left = None #Left child
        self.eq = None   #Equal    
        self.right = None #right

    def insert_in_tst(root, word):
        #this fuction inserts a word into the TST starting from the root
        if root is None:
            root = TSTNode(word[0])
        #if root is none, a new TST is created
            if len(word) == 1:
                root.is_end_of_string = True
        #if len = 1, the charac is a complete word, is_end_of_string is set to true

        #Recursive Insertion Logic
        if word[0] < root.data:
            root.left = TSTNode.insert_in_tst(root.left, word)
        #if word < data, its inserted in the left
        elif word[0] > root.data:
            root.right = TSTNode.insert_in_tst(root.right, word)
        #if word > data, to th right
        else: #if first character matches
            if len(word) > 1:
                root.eq = TSTNode.insert_in_tst(root.eq, word[1:])
                #insert rest of word in equal subtree
            else:
                root.is_end_of_string = True
                #mark end of string if its rhe last element
        return root
    #return rrot wich may be modified


    #non_recursive
    def search_tst_non_recursive(root, word):
        while root:
            if word[0] < root.data:
                root = root.left

            elif word[0] == root.data:
                if root.is_end_of_string and len(word) == 1:
                    return 1
                
                if len(word) > 1:
                    root = root.eq
                    word = word[1:]
                else:
                    return -1
        return -1

if __name__ == "__main__":
    # Example usage of LinearSearch
    arr = [10, 20, 30, 40, 50]
    print("Unordered Linear Search:", LinearSearch.unordered_linear_search(arr, len(arr), 30))
    print("Ordered Linear Search:", LinearSearch.ordered_linear_search(arr, len(arr), 30))

    # Example usage of Binary Search
    print("Binary Search Iterative:", LinearSearch.binary_search_iterative(arr, len(arr), 30))
    print("Binary Search Recursive:", LinearSearch.binary_search_recursive(arr, 0, len(arr) - 1, 30))

    # Example usage of Brute Force String Matching
    text = "hello world"
    pattern = "world"
    print("Brute Force Match:", StringAlgorithm.brute_force_match(text, len(text), pattern, len(pattern)))

    # Example usage of TrieNode
    root = TrieNode(None)
    TrieNode.search_in_trie(root, "")  # Example of searching in an empty Trie

    # Example usage of TSTNode
    tst_root = None
    tst_root = TSTNode.insert_in_tst(tst_root, "cat")
    tst_root = TSTNode.insert_in_tst(tst_root, "bat")
    tst_root = TSTNode.insert_in_tst(tst_root, "rat")
    print("Search TST Non-Recursive (cat):", TSTNode.search_tst_non_recursive(tst_root, "cat"))
    print("Search TST Non-Recursive (dog):", TSTNode.search_tst_non_recursive(tst_root, "dog"))