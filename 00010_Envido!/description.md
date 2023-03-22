[_Truco_](https://en.wikipedia.org/wiki/Truco) is a card game popular in South America in which players set up dialogs, bet for points, exchange information with gestures, and try to trick their opponents. It's breathtaking! 🔥

The exact rules of Truco vary from country to country. So now we want to calculate the value of the cards according to _envido_ - one of the bets that players can propose - in Argentina :flag_ar: . This is what we know:

* all cards from 1 to 7 inclusive are worth their numbering
* cards from 10 to 12 inclusive are worthless - their value is 0
* cards with 8 or 9 are never used in this card game.

> Define a function `envido_value` that takes a card rank and returns its _envido_ value:
>
> ```python
> ムenvido_value(12)
> 0
> ムenvido_value(3)
> 3
> ```
>
> :memo: Let's assume that we will never invoke `envido_value` with 8 or 9 as arguments.
