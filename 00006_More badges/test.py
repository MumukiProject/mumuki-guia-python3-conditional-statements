  
  def test_write_badge_Ana_Perez_false(self):
    self.assertEqual(write_badge("Ana", "Perez", "Backend Developer", False), "Ana Perez")
  
  def test_write_badge_Julio_Gelman_false(self):
    self.assertEqual(write_badge("Julio", "Gelman", "Helpdesk", False), "Julio Gelman")
  
  def test_write_badge_Ana_Perez_true(self):
    self.assertEqual(write_badge("Ana", "Perez", "Backend Developer", True), "Ana Perez, Backend Developer")
  
  def test_write_badge_Julio_Gelman_true(self):
    self.assertEqual(write_badge("Julio", "Gelman", "Helpdesk", True), "Julio Gelman, Helpdesk")
  
