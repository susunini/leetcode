class LRUCache(object):
    """ Design. Data Structure.
    
    Use a dictionary and a python list.
    Python list (array internally) is expensive with del and insert.
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.d = dict()
        self.li = list()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        
        idx = self.li.index(key)
        del self.li[idx]
        self.li.insert(0, key)
        return self.d[key]
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap < 1:
            return
        if key in self.d:
            idx = self.li.index(key)
            del self.li[idx]
        else:
            if len(self.li) == self.cap:
                del_key = self.li.pop()
                del self.d[del_key]
        self.d[key] = value
        self.li.insert(0, key)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node(object):
    """ Node in a double linked list """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache(object):
    """ Use a dictionary and a double linked list to keep record of
    LRU; Add two functions addNode and removeNode and all the operations
    with the double linked list can be done using these two functions.
    """
    def addNode(self, node):
        """ Add a node after head of the list """
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node
    
    def removeNode(self, node):
        """ Remove a node from the list """
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cnt = 0
        self.key_to_node = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.removeNode(node)
            self.addNode(node)
        else:
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.addNode(new_node)
            self.cnt += 1
            # caution: do not forget
            if self.cnt > self.cap:
                node_to_del = self.tail.prev
                del self.key_to_node[node_to_del.key]
                self.removeNode(node_to_del)
                self.cnt -= 1
        
