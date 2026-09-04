### Analysis data

**Note** *.remove() for TupleIndexableSet takes long to run but it works*

|Operation|ListIndexableSet |DictIndexableSet|TupleIndexableSet|
|-|-|-|-|
|.add() | 0.3211843967437744 s |0.5291292667388916 s | 0.37665724754333496 s |
|.contains() | 0.02967691421508789 s| 0.046343326568603516 s|0.025629281997680664 s |
|.get()| 5.507469177246094e-05 s|4.3392181396484375e-05 s|5.984306335449219e-05 s |
|.remove()|0.028095245361328125 s|0.3378636837005615 s|35.6006805896759 s |

###   Which implementation performed best for each operation? 

For .add() the best performance was shown in List implementation

For .contains() the best performance was shown in Tuple implementation

For .get() all of them show same performance but dictionaries are a little bit faster.

For .remove() the best performance was shown in List implementation

### Which structure feels most maintainable or convenient? 

The most maintainable implementation is the List implementation, since Lists are mutable, unlike Tuples and have normal indexing, unlike dictionaries. Which means that you can directly modify Lists without the need to create another one. Dictionary needs another dict for handling indexing, a tuple requires another tuple for basic addition or removal.

Moreover, lists have needed built-in functions, which make the implementation easier and more optimized.

### Describe the observed behavior based on execution time and ease of implementation

List is the best in terms of the ease of implementation as the needed functions are pre-defined, and List is mutable, meaning it must not perform unnecessary operations for functions changing the object elements.

Interesting part showing the importance of a type being mutable is .remove()'s tuple implementation, which took 35s to run because of the creation of many tuples through concatenation (+).