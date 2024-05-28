**What are Sets in Python?**

A set is an unordered collection of unique and immutable elements in Python. It is a mutable data structure, which means its elements can be added, removed, or modified.

**Creating a Set:**

```python
my_set = {1, 2, 3, 4}
```

**Properties of Sets:**

* **Unordered:** Elements are not stored in any particular order.
* **Unique:** Sets can contain only unique elements. Duplicates are ignored.
* **Immutable:** Elements cannot be modified. To change an element, the entire set must be recreated.

**Common Set Operations:**

* **Union (`set1.union(set2)`):** Returns a new set with all elements from both sets.
* **Intersection (`set1.intersection(set2)`):** Returns a new set with only elements that are in both sets.
* **Difference (`set1.difference(set2)`):** Returns a new set with elements that are in set1 but not in set2.
* **Symmetric Difference (`set1.symmetric_difference(set2)`):** Returns a new set with elements that are in either set but not both.
* **In Membership (`element in set`):** Checks if an element is present in the set.
* **Add (`set.add(element)`):** Adds an element to the set.
* **Remove (`set.remove(element)`):** Removes an element from the set.

**Example:**

```python
my_set1 = {1, 2, 3, 4}
my_set2 = {3, 4, 5, 6}

print(my_set1.union(my_set2))  # {1, 2, 3, 4, 5, 6}
print(my_set1.intersection(my_set2))  # {3, 4}
print(my_set1.difference(my_set2))  # {1, 2}
print(my_set1.symmetric_difference(my_set2))  # {1, 2, 5, 6}

my_set1.add(5)
my_set1.remove(3)

print(my_set1)  # {1, 2, 4, 5}
```

**Advantages of Sets:**

* Efficient for membership checks and set operations.
* Ensure uniqueness of elements.
* Used in sets theory and mathematical applications.

**Disadvantages of Sets:**

* Elements cannot be modified.
* Not suitable for ordered collections.
* May use more memory than lists or tuples.