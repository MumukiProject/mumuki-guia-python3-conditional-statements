One more thing! Sometimes we want just the first and last name on our :name_badge: badge, without the job title.

So we need to improve our function so that it receives 4 parameters:

1. the first name, as before;
1. the last name, as before;
1. the job title, as before;
1. a boolean value indicating whether we want a short badge with only the first and last name, or a long badge as before.

> Alter the function `write_badge`, so that it behaves as described above.
>
> ```python
> ムwrite_badge("Dana", "Velazquez", "Software Engineer", True)
> "Dana Velázquez, Software Engineer"
> ムwrite_badge( "Tomás", "Peralta", "Web Designer", False)
> "Tomás Peralta"
> ```
