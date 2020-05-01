from os import system, name 
import time
f1 =  [
"#",
" ",
" ",
" "
]
f2 =  [
" ",
"#",
" ",
" "
]
f3 =  [
" ",
" ",
"#",
" "
]
f4 =  [
" ",
" ",
" ",
"#"
]
f5 =  [
" ",
" ",
" ",
"#"
]
def printa(a):
  for b in a:
    print(b)
def play(fps):
  printa(f1)
  time.sleep(fps)
  clear()
  printa(f2)
  time.sleep(fps)
  clear()
  printa(f3)
  time.sleep(fps)
  clear()
  printa(f4)
  time.sleep(fps)
  clear()
  printa(f5)
  time.sleep(fps)
  clear()
  
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
play(.3)
