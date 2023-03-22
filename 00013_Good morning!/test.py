class Test(unittest.TestCase):

  def test_greetings_to_gus(self):
    self.assertEquals(greetings_to("Gus"), "Good morning Gus")
    
  def test_greetings_to_may(self):
    self.assertEquals(greetings_to("May"), "Good morning May")