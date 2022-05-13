import random
import os
import time, sys

#standard editions
wSchool = ("leraal", "tafel", "docenten", "kind", "toetsenbord", "concierge", "geodriehoek", "rekenmachine", "wiskunde", "natuurkunde", "scheikunde", "aardrijkskunde", "gangpad", "lokaal", "schrift", "pen", "potlood", "informatica", "informatica", "informatica")
wVerkeer = ("stopbord", "ongeluk", "auto", "vrachtwagen", "fiets")
editions = (wSchool, wVerkeer)
editions_names = ("school", "verkeer")
#special editions
w69 = ("uWu")
b_w69 = False #if triggered = true
w420 = ("wiet")
b_w420 = False#if triggered = true
w9854 = ("ei", "kip", 'schilderij', 'geheim') #easteregg edition

wlist = ''
w = ''
gw = ('w', 't') #guessed letters

def p(text):
  for letter in text:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.007)

def clear():
  os.system("clear")

def draw():
  blindword = []
  for l in list(w):
    if l in gw:
      blindword.append(l + '\u0332')
    else:
      blindword.append('_')
  print('  '.join(blindword))

if b_w69 == False and b_w420 == False:
    p("Kies je galgje editie!" 
   "\n\nKies uit:"
   "\n\n1 School"
   "\n2 Verkeer\n")
else:
    p("Kies je galgje editie!" 
   "\n\nKies uit:"
   "\n\n1    School"
   "\n2    Verkeer"
   "\n9854 ???\n")

wlist = ''
def chose():
  global wlist, b_w69, b_w420
  number = input()
  if number.isdigit():
    if int(number) <= len(editions) and int(number) > 0:
      wlist = editions[int(number)-1]
      wlistname = editions_names[int(number)-1]
      p(f"Je hebt voor {wlistname} gekozen")
      
      #special editions
    elif int(number) == 69:
      wlist = w69
      b_w69 = True
      p('Jij viezerik, je vraagt erom!')
    elif int(number) == 420:
      wlist = w420
      b_w420 = True
      p('Zet een raampje open!\nHet stikt hier van de rook!')
    elif int(number) == 9854:
      wlist = w9854
      p('Elk spel heeft wel een easteregg!')
      
    else:
      p("Deze editie is niet beschikbaar, better luck next time")
      return chose()
  else:
    p("Dat is geen getal, better luck next time")
    return chose()
time.sleep(2)
chose()
clear()
w = random.choice(wlist)
print(w)
draw()


      

def guess():
  guess = input()
  if guess.isaplha():
    if len(guess) > 1:
      if guess == w:
        win()
      else:
        fail()
    else:
      if guess in w:
        reveal()
      else:
        fail()
      
def reveal():
  print("reveal")
  
def fail():
  print("fail")
  
def lose():
  print('lose')

def win():
  print('win')