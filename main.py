from os import system, name 
import time
anim=[]
def play(fps):
 timer = fps
 for c in range(len(anim)):
  for b in anim[c]:
   if isinstance(b, float) == False: print(b)
   else: timer = b
 time.sleep(timer)
 if name == 'nt': _ = system('cls') 
 else: _ = system('clear')
 timer = fps
