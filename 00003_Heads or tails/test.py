  
  def test_decide_with_coin_heads_pizzas_empanadas_is_pizzas(self):
    self.assertEqual(decide_with_coin("heads", "pizzas", "empanadas"), "pizzas")

  def test_decide_with_coin_heads_asado_empanadas_is_asado(self):
    self.assertEqual(decide_with_coin("heads", "asado", "empanadas"), "asado")

  def test_decide_with_coin_tails_pizzas_empanadas_is_empanadas(self):
    self.assertEqual(decide_with_coin("tails", "pizzas", "empanadas"), "empanadas")

  def test_decide_with_coin_tails_pizzas_pastas_is_pastas(self):
    self.assertEqual(decide_with_coin("tails", "pizzas", "pastas"), "pastas")


