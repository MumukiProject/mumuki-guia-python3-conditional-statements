  
  def test_write_long_best_badge_when_name_is_carla_toledo(self):
    self.assertEqual(write_best_badge("Carla", "Toledo", "Data Analyst"), "Carla Toledo, Data Analyst")
  
  def test_write_long_best_badge_when_name_is_branco_luis(self):
    self.assertEqual(write_best_badge("Branco", "Luis", "Data Analyst"), "Branco Luis, Data Analyst")
  
  def test_write_ahort_best_badge_when_name_is_estanislao_schwarzschild(self):
    self.assertEqual(write_best_badge("Estanislao", "Schwarzschild", "Accountant"), "Estanislao Schwarzschild")
  
  def test_write_ahort_best_badge_when_name_is_katherine_boumann(self):
    self.assertEqual(write_best_badge("Katherine", "Boumann", "Accountant"), "Katherine Boumann")
    