In _truco_ another kind of bet can be proposed: the homonymous _truco_ bet.

It all starts by saying _"truco"_, and in response the opponents can optionally raise the bet. For example, if one player says _truco_, another player can reply _retruco_, and the value of the bet increases 📈:

<table class="table table-striped" align="center">
   <tr><th>Bet</th><th>Bet value</th></tr>
   <tr><td>truco</td><td>2</td></tr>
   <tr><td>retruco</td><td>3</td></tr>
   <tr><td>value cuatro</td><td>4</td></tr>
</table>

> Define the function `truco_value`, which takes the bet name and returns its value.
>
> ```python
> truco_value("truco")
> 2
> truco_value("retruco")
> 3
> ```
>
> :warning: Assume that `truco_value` will only be invoked with an argument that represents a proper bet name. For example, we are not going to test the function calling it like `truco_value("asdgh")`
