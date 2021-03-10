Ahora que ya vimos varios `if`s, volvamos a la función con la que iniciamos la lección: 

```python
ム saludar_a("Ivi", 17)
"Buenos días Ivi"
```

¿No es un poco tarde para decir _buen día_? :dizzy_face: ¿No sería mejor que `saludar_a` hiciera lo siguiente?

 1. Si son menos de las 12, que diga _Buenos días_;
 2. en caso contrario y si son menos de las 19, que diga _Buenas tardes_;
 3. en caso contrario, finalmente, que diga _Buenas noches_.
 
Sí, ¡eso es exactamente lo que queremos! Demos la bienvenida a un amigo inseperable del `if` y el `else`: el `elif`.

```python
def saludar_a(quien, horario):
  if horario < 12:
    return "Buenos días " + quien
  elif horario < 19:
    return "Buenas tardes " + quien
  else: 
    return "Buenas noches " + quien
```



