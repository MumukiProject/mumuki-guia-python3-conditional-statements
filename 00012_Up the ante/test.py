  
  def test_truco_value_retruco_is_3(self):
    self.assertEqual(truco_value("retruco"), 3)
  
  def test_truco_value_truco_is_2(self):
    self.assertEqual(truco_value("truco"), 2)
  
  def test_truco_value_vale_cuatro_is_4(self):
    self.assertEqual(truco_value("vale cuatro"), 4)
  
