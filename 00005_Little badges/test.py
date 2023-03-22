  
  def test_write_badge_Ana_Perez_backend_developer(self):
    self.assertEqual(write_badge("Ana", "Perez", "Backend Developer"), "Ana Perez, Backend Developer")
  
  def test_write_badge_Julio_Gelman_helpdesk(self):
    self.assertEqual(write_badge("Julio", "Gelman", "Helpdesk"), "Julio Gelman, Helpdesk")

