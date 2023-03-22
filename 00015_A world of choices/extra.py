def done(): 
  pass

def greet_to(who, hours):
  if hours < 12:
    return "Good morning " + who
  elif hours < 19:
    return "Good afternoon " + who
  else: 
    return "Good evening " + who
    
def greet_to_reloaded(who, hours):
  if hours < 19:
    return "Good afternoon " + who
  elif hours < 12:
    return "Good morning " + who
  else: 
    return "Good evening " + who
    