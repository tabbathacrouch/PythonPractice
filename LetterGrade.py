#LetterGrade

score = float(raw_input("Enter Score: "))
floatscore = type(score)
try:
  if score >= 0 and score <= 1.0:
    if score < 0.6:
      print "F"
    elif score >= 0.9:
      print "A"
    elif score >= 0.8:
      print "B"
    elif score >= 0.7:
      print "C"
    elif score >= 0.6:
      print "D"
  

    
  

    
except:
    print "error, not a number between 0.0 and 1.0!"
    