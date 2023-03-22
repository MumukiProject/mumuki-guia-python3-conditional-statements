class Test(unittest.TestCase):

  def test_greetings_to_gus(self):
    self.assertEquals(saludar_a("Gus"), "Good morning Gus")
    
  def test_greetings_to_may(self):
    self.assertEquals(saludar_a("May"), "Good morning May")