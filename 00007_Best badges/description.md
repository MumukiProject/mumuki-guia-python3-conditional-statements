Now that we're ready to compose both short and long badges, we need a function that creates badges of optimal size:

  * if first and last name have less than 15 letters in total, we want a long badge;
  * otherwise we want a short badge.

> Define the function `write_best_badge` that takes a title, a first name and a last name and generates a short or long poster, according to the previous rules.  For example:
>
> ```python
> ムwrite_best_badge("Carla", "Toledo", "Data Analyst")
> "Carla Toledo, Data Analyst"
> ムwrite_best_badge("Estanislao", "Schwarzschild", "Accountant")
> "Estanislao Schwarzschild"
> ```
> 
> `write_best_badge` must reuse `write_badge`.
