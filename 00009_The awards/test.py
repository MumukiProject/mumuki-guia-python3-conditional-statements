
  def test_medal_for_1(self):
    self.assertEqual(medal_for(1), "gold")

  def test_medal_for_2(self):
    self.assertEqual(medal_for(2), "silver")

  def test_medal_for_3(self):
    self.assertEqual(medal_for(3), "bronze")

  def test_medal_for_4(self):
    self.assertEqual(medal_for(4), "nothing")

  def test_medal_for_5(self):
    self.assertEqual(medal_for(5), "nothing")

  def test_medal_for_0(self):
    self.assertEqual(medal_for(0), "nothing")
    
    