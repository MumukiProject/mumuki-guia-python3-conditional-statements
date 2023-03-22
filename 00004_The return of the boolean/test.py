  
  # positives lower than 100 differents to 15
  
  def test_is_lucky_number_2_is_true(self):
    self.assertTrue(is_lucky_number(2))

  def test_is_lucky_number_5_is_true(self):
    self.assertTrue(is_lucky_number(5))

  def test_is_lucky_number_9_is_true(self):
    self.assertTrue(is_lucky_number(9))

  def test_is_lucky_number_45_is_true(self):
    self.assertTrue(is_lucky_number(45))
    
  def test_is_lucky_number_97_is_true(self):
    self.assertTrue(is_lucky_number(97))  
    
  # greater than 100
  
  def test_is_lucky_number_101_is_false(self):
    self.assertFalse(is_lucky_number(101))

  def test_is_lucky_number_12456_is_false(self):
    self.assertFalse(is_lucky_number(12456))

  def test_is_lucky_number_3003_is_false(self):
    self.assertFalse(is_lucky_number(3003))

  # negatives

  def test_is_lucky_number_is_false_if_it_is_negative(self):
    self.assertFalse(is_lucky_number(-3))

  # is 15

  def test_is_lucky_number_15_is_false(self):
    self.assertFalse(is_lucky_number(15))
