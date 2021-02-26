  
  def test_puntosDeEnvidoTotales_4_espadas_3_espadas_es_27(self):
    self.assertEqual(puntos_de_envido_totales(4, "espadas", 3, "espadas"), 27)
  
  def test_puntosDeEnvidoTotales_6_copas_11_copas_es_26(self):
    self.assertEqual(puntos_de_envido_totales(6, "copas", 11, "copas"), 26)
  
  def test_puntosDeEnvidoTotales_8_oro_2_bastos_es_8(self):
    self.assertEqual(puntos_de_envido_totales(5, "oro", 2, "bastos"), 5)
  
  def test_puntosDeEnvidoTotales_6_copas_7_espadas_es_7(self):
    self.assertEqual(puntos_de_envido_totales(6, "copas", 7, "espadas"), 7)
  
