
  def test_sign_10_is_1(self):
    self.assertEqual(sign(10), 1)

  def test_sign_1_is_1(self):
    self.assertEqual(sign(1), 1)

  def test_sign_0_is_0(self):
    self.assertEqual(sign(0), 0)

  def test_sign_negative_65_is_negative_1(self):
    self.assertEqual(sign(-65), -1)

  def test_sign_negative_87_is_negative_1(self):
    self.assertEqual(sign(-87), -1)


