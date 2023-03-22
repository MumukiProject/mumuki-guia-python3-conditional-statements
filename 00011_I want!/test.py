  
  def test_total_envido_points_4_swords_3_swords_is_27(self):
    self.assertEqual(total_envido_points(4, "swords", 3, "swords"), 27)
  
  def test_total_envido_points_6_cups_11_cups_is_26(self):
    self.assertEqual(total_envido_points(6, "cups", 11, "cups"), 26)
  
  def test_total_envido_points_5_coins_2_clubs_is_5(self):
    self.assertEqual(total_envido_points(5, "coins", 2, "clubs"), 5)
  
  def test_total_envido_points_6_cups_7_swords_is_7(self):
    self.assertEqual(total_envido_points(6, "cups", 7, "swords"), 7)
    
  def test_total_envido_points_1_cups_12_swords_is_1(self):
    self.assertEqual(total_envido_points(1, "cups", 12, "swords"), 1)
  
