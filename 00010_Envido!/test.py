  
  def test_envido_value_2_is_2(self):
    self.assertEqual(envido_value(2), 2)
  
  def test_envido_value_1_is_1(self):
    self.assertEqual(envido_value(1), 1)
  
  def test_envido_value_5_is_5(self):
    self.assertEqual(envido_value(5), 5)
    
  def test_envido_value_7_is_7(self):
    self.assertEqual(envido_value(7), 7)  
  
  def test_envido_value_12_is_0(self):
    self.assertEqual(envido_value(12), 0)
  
  def test_envido_value_11_is_0(self):
    self.assertEqual(envido_value(11), 0)
  
  def test_envido_value_10_is_0(self):
    self.assertEqual(envido_value(10), 0)
