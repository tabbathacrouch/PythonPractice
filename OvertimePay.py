#Overtime Pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
ratehr = raw_input("Enter Rate per Hour:")
r = float(ratehr)

if h < 40:
  grosspay1 = h * r
  print grosspay1
elif h >= 40:
  exthrs = h - 40 
  newr = r * 1.5
  grosspay2 = (40 * r) + (exthrs * newr)
  print grosspay2

