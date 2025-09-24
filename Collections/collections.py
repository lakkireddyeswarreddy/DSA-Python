"""
Collections is a module in Python that provides alternatives to built-in data types such as lists, tuples, and dictionaries. It includes specialized container datatypes that can be used to store and manipulate data more efficiently.
Collections module includes the following classes:
- namedtuple(): Factory function for creating tuple subclasses with named fields.
- deque: List-like container with fast appends and pops on either end.
- Counter: A dict subclass for counting hashable objects.   
- OrderedDict: A dict subclass that remembers the order entries were added.
- defaultdict: A dict subclass that calls a factory function to supply missing values.
- ChainMap: A class for creating a single view of multiple mappings.

Here is a brief overview of each class:
1. namedtuple(): It is used to create tuple-like objects with named fields. This makes the code more readable and self-documenting.
   Example:
   from collections import namedtuple
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(10, 20)
   print(p.x, p.y)  # Output: 10 20
   
2. deque: It is a double-ended queue that allows you to append and pop elements from both ends with O(1) time complexity.
   Example:
    from collections import deque
    d = deque([1, 2, 3])
    d.appendleft(0)
    d.append(4)
    print(d)  # Output: deque([0, 1, 2, 3, 4])
    d.pop()
    d.popleft()
    print(d)  # Output: deque([1, 2, 3])
    
3. Counter: It is a subclass of dict that is used to count hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
   Example:
    from collections import Counter
    c = Counter('hello world')
    print(c)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    
4. OrderedDict: It is a subclass of dict that maintains the order in which the keys were added. This is useful when the order of elements matters.
    Example:
     from collections import OrderedDict
     od = OrderedDict()
     od['a'] = 1
     od['b'] = 2
     od['c'] = 3
     print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
     
5. defaultdict: It is a subclass of dict that provides a default value for a nonexistent key. This is useful when you want to avoid KeyError exceptions.
    Example:
     from collections import defaultdict
     dd = defaultdict(int)
     dd['a'] += 1
     dd['b'] += 2
     print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})  
     
6. ChainMap: It is a class that groups multiple dictionaries or mappings together to create a single, updateable view.  
    Example:
     from collections import ChainMap
     dict1 = {'a': 1, 'b': 2}
     dict2 = {'b': 3, 'c': 4}
     cm = ChainMap(dict1, dict2)
     print(cm)  # Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
     print(cm['b'])  # Output: 2 (from dict1)
     this is because ChainMap searches the dictionaries from left to right and returns the first match it finds.
     print(cm['c'])  # Output: 4 (from dict2)   
    cm['b'] = 5
    This will update 'b' in dict1 since it is the first mapping in the ChainMap.
    print(cm)  # Output: ChainMap({'a': 1, 'b': 5}, {'b': 3, 'c': 4})
        
"""