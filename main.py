import random
import os
import time, sys

#standard editions
wSchool = ("leraal", "tafel", "docenten", "kind", "toetsenbord", "concierge", "geodriehoek", "rekenmachine", "wiskunde", "natuurkunde", "scheikunde", "aardrijkskunde", "gangpad", "lokaal", "schrift", "pen", "potlood", "informatica", "informatica", "informatica")
wVerkeer = ("stopbord", "ongeluk", "auto", "vrachtwagen", "fiets", 'verkeer')
editions = (wSchool, wVerkeer)
editions_names = ("school", "verkeer")
#special editions
w69 = ("uwu", 'sex', 'porn')
b_w69 = False #if triggered = true
w420 = ("wiet", 'aansteker', 'roken')
b_w420 = False#if triggered = true
w9854 = ("ei", "kip", 'schilderij', 'geheim') #easteregg edition

wlist = '' #chosen word list
w = '' #word
gl = ['t', 'g'] #guessed letters/words
gw = ['toot']
lives = 5

def p(text): #animated text
  for l in text:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.07)

def clear(): #clear console
  os.system("clear")
clear()

def lose():
  clear()
  p(f'Je hebt helaas verloren\nHet woord was : {w}\nWil je het opnieuw proberen typ dan ja, als je dit niet wilt typ dan nee:')
  replay = input()
  if replay == "ja":
    clear()
    return editiebegin()
  elif replay == "nee":
    p("jammer weer dit :(")
    quit
  else:
    p("je hebt geen ja of nee ingetypt")
    return

def win():
  p(f'\nJe hebt gewonnen :)\nHet woord was : {w}\nWil je opnieuw spelen typ dan ja zoniet typ nee:')
  replay = input()
  if replay == "ja":
    clear()
    return editiebegin()
  elif replay == "nee":
    p("jammer weer dit :(")
    quit
  else:
    p("je hebt geen ja of nee ingetypt")
    return

def reveal(guess):
  gl.append(guess)
  if guess == w:
    win()
  p("Deze letter zit in het woord :)")
  return draw()
  
def fail(guess):
  global lives
  if len(guess) >= 2:
    gw.append(guess)
  else:
    gl.append(guess)
  lives = lives - 1
  if lives == 0:
    lose()
  p("Deze letter zit helaas niet in het woord :(\n")
  return draw()

def guess(): #check if letter/word is matching
  guess = input().lower()
  if guess.isalpha():
    if guess not in gl or guess not in gw:
      if len(guess) > 1:
        if guess == w:
          win()
        else:
          fail(guess)
      else:
        if guess in w:
          reveal(guess)
        else:
          fail(guess)
    else:
      p("Dit heb je al een keer geprobeerd te raden. Probeer een andere letter of woord.")
  else:
    p("Dat is geen letter of woord, better luck next time\n")
    return

def draw(): #print state of game
  clear()
  blindedword = []
  p(f'Type een letter of een woord om het woord te raden.\n\npogingen over: {lives}\n')
  for l in list(w):
    if l in gl:
      blindedword.append(l + '\u0332')
    else:
      blindedword.append('_')
  p('  '.join(blindedword))
  p('\n\nFout geraden letters: ')
  wgl = [] # wrong guessed letters
  for l in gl:
    if l not in w:
      wgl.append(l)
  p(', '.join(wgl))
  p('\n')
  p('Fout geraden woorden: ')
  p(', '.join(gw))
  p('\n')
  guess()
  
def chose(): #chose edition
  global wlist, b_w69, b_w420, w
  number = input()
  if number.isdigit():
    if int(number) <= len(editions) and int(number) > 0:
      wlist = editions[int(number)-1]
      wlistname = editions_names[int(number)-1]
      p(f"Je hebt voor {wlistname} gekozen")
      w = random.choice(wlist) #chose word
      draw()
      #special editions
    elif int(number) == 69:
      wlist = w69
      b_w69 = True
      p('Jij viezerik, je vraagt erom!')
      w = random.choice(wlist) #chose word
      draw()
    elif int(number) == 420:
      wlist = w420
      b_w420 = True
      p('Zet een raampje open!\nHet stikt hier van de rook!')
      w = random.choice(wlist) #chose word
      draw()
    elif int(number) == 9854:
      wlist = w9854
      p('Elk spel heeft wel een easteregg!')
      w = random.choice(wlist) #chose word
      draw()
    else:
      p("Deze editie is niet beschikbaar, better luck next time\n")
      return
  else:
    p("Dat is geen getal, better luck next time\n")
    return chose()
    
def editiebegin():
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
  chose()

editiebegin()