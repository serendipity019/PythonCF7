sym = {
    "key1" : "value1",
    "key2" : 10,
    3 : [100, 200, 300],
    4 : {"nested_key1": "nested_value1", "nested_key2": "nested_value2"},
  # [1, 2, 3] : "This is a list as a key",  # This will raise a TypeError since lists are not hashable
    (1, 2) : "This is a tuple as a key",  # This is valid since tuples are hashable
  # {1, 2} : "This is a set as a key",  # This will raise a TypeError since sets are not hashable
    frozenset({1, 2}) : "This is a frozenset as a key"  # This is valid since frozensets are hashable

}