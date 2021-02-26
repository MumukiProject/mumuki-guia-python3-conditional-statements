Ninguna introducción al lenguaje Python estaría completa sin mostrar al menos una estructura de control que ya conocemos: ¡la alternativa condicional! Veamos un ejemplo:


```python
# Equivalente a abs
def valor_absoluto(numero):
  if numero >= 0:
    return numero
  else:
    return -numero
```

> Veamos si se entiende: escribí una función `maximo`, que funcione como `max` (¡no vale usarla!) y devuelva el máximo entre dos números. Por ejemplo, el máximo entre 4 y 5 es 5, y el máximo entre 10 y 4, es 10.
