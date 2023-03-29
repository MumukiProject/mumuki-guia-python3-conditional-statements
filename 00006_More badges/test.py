  
  def test_write_badge_Ana_Perez_false_must_write_a_short_badge(self):
    self.assertEqual(write_badge("Ana", "Perez", "Backend Developer", False), "Ana Perez")
  
  def test_write_badge_Julio_Gelman_false_must_write_a_short_badge(self):
    self.assertEqual(write_badge("Julio", "Gelman", "Helpdesk", False), "Julio Gelman")
  
  def test_write_badge_Ana_Perez_true_must_write_a_long_badge(self):
    self.assertEqual(write_badge("Ana", "Perez", "Backend Developer", True), "Ana Perez, Backend Developer")
  
  def test_write_badge_Julio_Gelman_true_must_write_a_long_badge(self):
    self.assertEqual(write_badge("Julio", "Gelman", "Helpdesk", True), "Julio Gelman, Helpdesk")
  
