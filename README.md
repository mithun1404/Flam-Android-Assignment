# Flam-Android-Assignment (SET - 1)
## QUESTION - 1


<!-- description:start -->

<p>Design and implement a Least Recently Used (LRU) Cache. A cache has a fixed capacity, and when it exceeds that capacity, it must evict the least recently used item to make space for the new one.
.</p>

<p>The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;LRUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>Explanation</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>Maximum number of operations <code>10<sup>5</sup></code> calls will be made to <code>get</code> and <code>put</code>.</li>
	


</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Doubly Linked List

We can implement an LRU (Least Recently Used) cache using a "hash table" and a "doubly linked list".

-   Hash Table: Used to store the key and its corresponding node location.
-   Doubly Linked List: Used to store node data, sorted by access time.

When accessing a node, if the node exists, we delete it from its original position and reinsert it at the head of the list. This ensures that the node stored at the tail of the list is the least recently used node. When the number of nodes exceeds the maximum cache space, we eliminate the node at the tail of the list.

When inserting a node, if the node exists, we delete it from its original position and reinsert it at the head of the list. If it does not exist, we first check if the cache is full. If it is full, we delete the node at the tail of the list and insert the new node at the head of the list.

The time complexity is $O(1)$, and the space complexity is $O(\textit{capacity})$.


## QUESTION - 2
You are required to implement a simplified version of a HashMap (also known as an unordered map or dictionary), **without using any built-in hash table libraries** such as `dict`, `map`, or `unordered_map`.

Design a data structure that supports the following operations in **average-case O(1)** time:

### Supported Operations

- `put(key, value)`: Insert or update the value associated with a key.
- `get(key)`: Retrieve the value for a given key. Return `-1` if the key doesn't exist.
- `remove(key)`: Delete the key-value pair from the map.

### Constraints

- All keys and values are integers.
- `0 <= key, value <= 10^6`
- Up to `10^5` operations.
- Keys are unique within the map.
- Built-in hash table structures are **not allowed**.

---

## 💡 Approach

We implement a **custom hash map** using:

- A fixed-size list of buckets.
- **Hash Function**: `key % number_of_buckets`.
- **Separate Chaining**: Each bucket holds a list of `(key, value)` pairs.

This design ensures average-case **O(1)** time complexity for `put`, `get`, and `remove` operations.

---

## 🧪 Example Usage

```python
obj = MyHashMap()
obj.put(1, 10)       # inserts key 1 with value 10
obj.put(2, 20)       # inserts key 2 with value 20
print(obj.get(1))    # returns 10
print(obj.get(3))    # returns -1 (not found)
obj.put(2, 30)       # updates key 2 with new value 30
print(obj.get(2))    # returns 30
obj.remove(2)        # removes key 2
print(obj.get(2))    # returns -1
```
