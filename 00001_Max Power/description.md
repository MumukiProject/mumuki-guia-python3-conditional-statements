Let's look at another example...

```python
# equivalent to abs
def absolute_value(number):
  if number >= 0:         # 1.
    return number         # 2.
  else:
    return -number        # 3.
```

...and give a name to each part of the `if` conditional statement:

 1. First, there is a _condition_, that determines which action is going to be executed. It can be any **boolean expression**, or in - in simpler terms - anything that represents a "question" that can be answered as yes (`True`) or no (`False`);
 2. then there is _an `if` action_, which will return what we need when the aforementioned condition is `True`;
 3. Finally there is _an `else` action_, which will return what we need when the aforementioned condition is `False`.

Furthermore, these actions are also called _branches_ :deciduous_tree: because they branch the execution flow and introduce alternative flows into our programs.  Oh, one more thing: the tabs `↹` in each branch are essential for everything to work. :sweat_smile:

> Let's write our first `if`! Define a function `maximum`, that works like `max` and returns the maximum between two numbers:
>
> ```python
> ムmaximum(4, 5)
> 5
> ムmaximum(10, 4)
> 10
> ```
