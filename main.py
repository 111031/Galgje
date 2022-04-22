import random
import time, sys

wSchool = ("leraal", "tafel", "docenten", "kind", "toetsenbord", "concierge", "geodriehoek", "rekenmachine", "wiskunde", "natuurkunde", "scheikunde", "aardrijkskunde", "gangpad", "lokaal", "schrift", "pen", "potlood", "informatica", "informatica", "informatica")
wVerkeer = ("stopbord", "ongeluk", "auto", "vrachtwagen", "fiets")
editions = (wSchool, wVerkeer)
editions_names = ("school", "verkeer")

def p(text):
  for letter in text:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.0007)

p("Kies je galgje editie!" 
 "\n\nKies uit:"
 "\n\n1 School"
 "\n2 Verkeer\n")
wlist = ''
def chose():
  number = input()
  if number.isdigit():
    if int(number) <= len(editions) and int(number) > 0:
      wlist = editions[int(number)-1]
      wlistname = editions_names[int(number)-1]
      p(f"Je hebt voor {wlistname} gekozen")
    else:
      p("deze editie is niet beschikbaar, better luck next time")
      return chose()
  else:
    p("dat is geen getal, better luck next time")
    return chose()
chose()