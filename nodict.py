#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Ruben Espino with Paul Racisz'


class Node:
    """Stores key values in a hashtable"""
    def __init__(self, key, value=None):
        """
        Init takes key and value.
        Key is needed.
        Value is not.
        """
        self.key = key
        self.value = value
        self.hash = hash(key)

    def __repr__(self):
        """Retruns a string representing Node object."""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """
        Keys of two objects and compares them to see if they are equal.
        Returns Boolean.
        """
        return self.key == other.key


class NoDict:
    """Python dict without using built in methods to make a dict"""
    def __init__(self, num_buckets=10):
        """
        Class initializer to create the buckets according to a size parameter.
        If nothing is given then default is 10.
        """
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                          for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """
        This class method should accept a new key and value,
        and store it into the bucket
        """
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for i in bucket:
            if i == new_node:
                bucket.remove(i)
                break
        bucket.append(new_node)

    def get(self, key):
        """
        This class method should perform a key-lookup in the NoDict class.
        It should accept just one parameter: The key to look up.
        If the key is found in the NoDict class,
        return its associated value.
        If the key is not found, raise a KeyError exception.
        """
        node_to_find = Node(key)
        bucket = self.buckets[node_to_find.hash % self.size]
        for i in bucket:
            if i == node_to_find:
                return i.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """
        Implement this magic "dunder" method within the NoDict class
        to enable square-bracket reading behavior.
        """
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """
        Implement this magic "dunder" method within the NoDict class
        to enable square-bracket assignment behavior.
        """
        self.add(key, value)
