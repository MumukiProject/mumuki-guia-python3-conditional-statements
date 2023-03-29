Actually, we don't always greet with a _good morning_: when night falls, for example, we say _good evening_. :night_with_stars:

Therefore, we are going to modify our `greet_to` function so that it takes an additional parameter, `hour`, and returns a different _salutation_:

```python
ム greet_to("Dani", 10)
"Good morning Dani"
ム greet_to("Feli", 22)
"Good evening Feli"
```

But how could we accomplish this? No introduction to the Python language would be complete without showing _the_ most iconic control structure in programming: the conditional statement!

```python
def greet_to(who, hour):
  if hour < 19:
    return "Good morning " + who
  else:
    return "Good evening " + who
```

> :hourglass_flowing_sand: Take a few minutes to read this `if` and try to understand what is happening here. When you’re done, try doing the following in the console by calling `greet_to` :
>
> 1. Say hello to `"Umi"` at `18`
> 2. Say hello to `"Pun Pun"` at `19`
>
> What happens? Is this what you expected? :thinking:



