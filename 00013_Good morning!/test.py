class Test(unittest.TestCase):

  def test_greet_to_gus(self):
    self.assertEquals(greet_to("Gus"), "Good morning Gus")
    
  def test_greet_to_may(self):
    self.assertEquals(greet_to("May"), "Good morning May")