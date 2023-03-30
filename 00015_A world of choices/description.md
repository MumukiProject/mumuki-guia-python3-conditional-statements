Now that we've covered several `if`s, let's go back to the function we started the lesson with:

```python
ム greet_to("Umi", 17)
"Good morning Umi"
```

Isn't it a little late to say _good morning_? :dizzy_face: Wouldn't it be better if `greet_to` did the following?

 1. If it's less than 12, say _Good morning_;
 2. **else**, **if** it's less than 7:00 p.m., say _Good afternoon_;
 3. **else** and at last, say _Good evening_.
 
🎊 Yes, that's exactly what we want! Let's welcome the best friend of `if` and `else` statements: `elif`.

```python
def greet_to(who, hour):
  if hour < 12:
	  return "Good morning " + who
  elif hour < 19:
	  return "Good afternoon " + who
  else:
	  return "Good evening " + who
```

As we can see, with `elif` we can make a decision when the previous condition isn't met, and as the name suggests, it works like combining an `if` right after an `else`.

> :warning: Does this mean that the conditions are evaluated **in order**? Will this alternative definition...
>
> ```python
> def greet_to_reloaded(who, hours):
>   if hours < 19:
>	    return "Good afternoon " + who
>   elif hours < 12:
>	    return "Good morning " + who
>   else:
>	    return "Good evening " + who
> ```
>
> ...work exactly as the previous one? We have already defined `greet_to` and `greet_to_reloaded` and loaded them into the console so that you can try and compare them.
>
> When you're done, enter `done()`.
