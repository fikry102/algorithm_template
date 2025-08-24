# 使用 Python3 写算法题

这里简单介绍使用 Python3 写算法题时的一些特点。本项目并不是一个 Python3 教程，所以默认大家对 Python3 有一定的了解，对于零基础的同学建议首先了解一下 Python3 的基本语法等基础知识。

## 逻辑

进行 coding 面试时，如果不指定使用的编程语言，一般来讲考察的是做题的思路而不是编程本身，因此不需要从零开始实现一些基础的数据结构或算法，利用语言的一些特性和自带的标准库可以大大简化代码，提高做题速度。下面会总结一些 Python3 常用的特性，标准算法和数据结构。

## 常用特性

Python语言有很多特性可以大大简化代码，下面列举几个常用的。

#### 数组初始化

```Python
# 初始化一个长度为 N 的一维数组
Array = [0] * N

# 初始化一个形状为 MxN 的二维数组(矩阵)
Matrix = [[0] * N for _ in range(M)] # 思考：可以写成 [[0] * N] * M 吗？
```



```python
matrix = [[0] * 3] * 2
# 等价于：
# row = [0, 0, 0]
# matrix = [row, row]  → 两个引用指向同一个列表！

matrix[0][0] = 99
print(matrix)
# 输出：
# [[99, 0, 0],
#  [99, 0, 0]]  ❌ 所有行都变了！

```



#### 交换元素值

```Python
# c语言风格的交换两个元素值
tmp = a
a = b
b = tmp

# python风格
a, b = b, a
```

#### 连续不等式或等式

```Python
# 判断 a，b，c 是否相等，Python里可以直接写连等
if a == b == c:
    return True

# 不等式也可以
if a <= b < c:
    return True
```

## 标准算法

#### 排序

Python 中排序主要使用 sorted() 和 .sort() 函数，在[官网](https://docs.python.org/3/howto/sorting.html)有详细介绍，大家可以自行阅读。

A simple ascending sort is very easy: just call the sorted() function. It returns a new sorted list:

```python
sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
```

You can also use the list.sort() method. It modifies the list in-place (and returns None to avoid confusion). Usually it’s less convenient than sorted() - but if you don’t need the original list, it’s slightly more efficient.

```python
a = [5, 2, 3, 1, 4]
a.sort()
a
[1, 2, 3, 4, 5]
```

Another difference is that the list.sort() method is only defined for lists. In contrast, the sorted() function accepts any iterable.

```python
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
```



#### 二分查找和插入

Python 自带的 [bisect](https://docs.python.org/3/library/bisect.html) 库可以实现二分查找和插入，非常方便。



`bisect` 用于在**有序列表**中二分查找或插入。

`bisect` 这个名字来自 **“bisection” = 二分法**，意思是：

- 在一个有序区间里，不断对半切分（bisect），直到找到元素的位置或插入点。
- 所以 `bisect_left`、`bisect_right` 就是“二分法查找左/右插入点”

```python
import bisect
a = [1, 3, 4, 4, 5, 7]

#查找
bisect.bisect_left(a, 4)   # 2, 第一个 ≥4 的位置
bisect.bisect_right(a, 4)  # 4, 第一个 >4 的位置
bisect.bisect(a, 4)        # 4, 等价于 bisect_right

#插入
a = [1, 3, 4, 4, 5]
bisect.insort_left(a, 4)   # 插在第一个 4 的左边
# [1, 3, 4, 4, 4, 5]

a = [1, 3, 4, 4, 5]
bisect.insort(a, 4)        # 插在最后一个 4 的右边
# [1, 3, 4, 4, 4, 5]


```



## 标准数据结构

#### 栈

Python 中的栈使用自带的 list 类来实现，可参考[官方文档](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)。

```python
>>>stack = [3, 4, 5]
>>>stack.append(6)
>>>stack.append(7)
>>>stack
[3, 4, 5, 6, 7]
>>>stack.pop()
7
>>>stack
[3, 4, 5, 6]
>>>stack.pop()
6
>>>stack.pop()
5
>>>stack
[3, 4]
```



#### 队列

使用 collections 库中的 deque 类实现，可参考[官方文档](https://docs.python.org/3/library/collections.html#collections.deque)。

```python
>>>from collections import deque
>>>d = deque('ghi')                 # make a new deque with three items
>>>for elem in d:                   # iterate over the deque's elements
...    print(elem.upper())
G
H
I

>>>d.append('j')                    # add a new entry to the right side
>>>d.appendleft('f')                # add a new entry to the left side
>>>d                                # show the representation of the deque
deque(['f', 'g', 'h', 'i', 'j'])

>>>d.pop()                          # return and remove the rightmost item
'j'
>>>d.popleft()                      # return and remove the leftmost item
'f'
>>>list(d)                          # list the contents of the deque
['g', 'h', 'i']
>>>d[0]                             # peek at leftmost item
'g'
>>>d[-1]                            # peek at rightmost item
'i'
```



#### 堆

Python 中没有真的 heap 类，实现堆是使用 list 类配合 heapq 库中的堆算法，且只支持最小堆，最大堆需要通过传入负的优先级来实现，可参考[官方文档](https://docs.python.org/3.8/library/heapq.html)。

heapify(), heappush(), heappop()

```python
>>> import heapq

>>> # Start with an unsorted list of numbers
>>> data = [3, 5, 1, 9, 4, 8, 2]
>>> data
[3, 5, 1, 9, 4, 8, 2]

>>> # Convert the list into a min-heap, in-place
>>> heapq.heapify(data)
>>> # The list now satisfies the heap property
>>> data
[1, 3, 2, 9, 4, 8, 5]

>>> # The top of the heap is always the smallest element
>>> data[0]
1

>>> # Push a new item onto the heap
>>> heapq.heappush(data, 0)
>>> # The new smallest item is now at the top
>>> data
[0, 1, 2, 3, 4, 8, 5, 9]
>>> data[0]
0

>>> # Pop and return the smallest item from the heap
>>> heapq.heappop(data)
0

>>> # The heap is rearranged after popping
>>> data
[1, 3, 2, 9, 4, 8, 5]
>>> # The new smallest item is at the top again
>>> data[0]
1

```



#### HashSet，HashTable

分别通过 [set 类](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset)和 [dict 类](https://docs.python.org/3/library/stdtypes.html#typesmapping)来实现。

```python
>>> # Create a set from a list with duplicate items
>>> items = ['apple', 'banana', 'orange', 'apple', 'banana']
>>> unique_items = set(items)
>>> # Note that the duplicates are automatically removed
>>> unique_items
{'orange', 'banana', 'apple'}

>>> # Add a new item
>>> unique_items.add('grape')
>>> unique_items
{'orange', 'grape', 'banana', 'apple'}

>>> # Adding an existing item does nothing
>>> unique_items.add('apple')
>>> unique_items
{'orange', 'grape', 'banana', 'apple'}

>>> # Fast membership testing (the main strength of a set)
>>> 'banana' in unique_items
True
>>> 'mango' in unique_items
False
```



```python
>>> # A list of words from a document
>>> words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

>>> # Use a dictionary to count the frequency of each word
>>> word_counts = {}
>>> for word in words:
...     word_counts[word] = word_counts.get(word, 0) + 1
...
>>> word_counts
{'apple': 3, 'banana': 2, 'orange': 1}

>>> # Iterate over the key-value pairs in the dictionary
>>> for word, count in word_counts.items():
...     print(f'The word "{word}" appeared {count} times.')
...
The word "apple" appeared 3 times.
The word "banana" appeared 2 times.
The word "orange" appeared 1 times.

```



## collections 库

Python 的 [collections 库](https://docs.python.org/3/library/collections.html)在刷题时会经常用到，它拓展了一些Python中基础的类，提供了更多功能，例如 defaultdict 可以预设字典中元素 value 的类型，自动提供初始化，Counter 可以直接统计元素出现个数等。



### `collections.defaultdict`

A `defaultdict` is a subclass of the standard `dict`. The key difference is that it never raises a `KeyError`. Instead, if you try to access a key that doesn't exist, it automatically creates a default value for that key using a "factory" function you provide.

This is incredibly useful for grouping or counting items, as it saves you from writing extra `if key in my_dict:` checks.

```python
>>> from collections import defaultdict

>>> # A list of words
>>> words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

>>> # We provide `int` as the factory. int() returns 0.
>>> word_counts = defaultdict(int)
>>> for word in words:
...     word_counts[word] += 1 # If 'word' is new, its value is created as 0, then incremented.
...
>>> word_counts
defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})

>>> # Accessing a non-existent key returns the default value (0)
>>> word_counts['mango']
0

```

### `collections.Counter`

A `Counter` is a specialized `dict` subclass designed specifically for counting hashable objects. It's like a `defaultdict(int)` but with extra, powerful methods.

#### Example 1: The Easiest Way to Count

`Counter` can be initialized directly from any iterable.

```python
>>> from collections import Counter

>>> # A list of words
>>> words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

>>> # One-liner to count everything!
>>> word_counts = Counter(words)
>>> word_counts
Counter({'apple': 3, 'banana': 2, 'orange': 1})

>>> # It works like a dictionary
>>> word_counts['apple']
3

>>> # Like defaultdict(int), it returns 0 for missing items instead of raising an error
>>> word_counts['mango']
0
```





## 总结

以上列举了一些用 Python3 做算法题时可以用到的一些特性，标准算法和数据结构，总结得肯定不全，因为 Python3 真的有很多可以利用的"神操作"，大家在学习本项目的时候也会见到，一下记不住也没关系，多实战就会了。