Now that we're ready to compose both short and long badges, we need a function that creates badges of optimal size:

  * if first and last name have more than 15 letters in total, we want a short badge;
  * otherwise we want a long badge.

> Define the function `write_best_badge` that takes a title, a first name and a last name, and calling `write_poster` generates a short or long poster, according to the previous rules. For example:
>
> ```python
> ムwrite_best_badge("Carla", "Toledo", "Data Analyst")
> "Carla Toledo, Data Analyst"
> ムwrite_best_badge("Estanislao", "Schwarzschild", "Accountant")
> "Estanislao Schwarzschild"
> ```
