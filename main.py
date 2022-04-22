import random
import time, sys

wSchool = ("leraal", "tafel", "docenten", "kind", "toetsenbord", "concierge", "geodriehoek", "rekenmachine", "wiskunde", "natuurkunde", "scheikunde", "aardrijkskunde", "gangpad", "lokaal", "schrift", "pen", "potlood", "informatica", "informatica", "informatica")
wVerkeer = ("stopbord", "ongeluk", "auto", "vrachtwagen", "fiets")
editions = (wSchool, wVerkeer)

def p(text):
  for letter in text:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.07)

p("Kies je galgje editie!" 
 "\n\nKies uit:"
 "\n\n1 School"
 "\n2 Verkeer\n")

number = input()
if int(number) == 1:
  print(number)