To sum up, now that we've seen how to write conditional statements, it's time for a friendly reminder: ⚠️ _if you use boolean expressions properly, you don't always need an `if`!_

For example, we might be tempted to rewrite the `is_adult` function we defined earlier:

```python
def is_adult(age):
  if age >= 18:
    return True
  else:
    return False
```

However, **this `if` is completely unnecessary**, since the boolean expression `age >= 18` is, ahem, already a boolean 😝:

```python
def is_of_age(age):
  return age >= 18
```

Much simpler, right? :wink:

> For May, a number is lucky if:
>
> * is positive, and
> * is less than 100, and
> * is not 15.
>
> Define the function `is_lucky_number` which, given a number, returns whether it complies with the previous logic. It's no use using `if`!
