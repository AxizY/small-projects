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

def play(fps):
  print(f1)
  time.sleep(fps)
  clear()
  print(f2)
  time.sleep(fps)
  clear()
  print(f3)
  time.sleep(fps)
  clear()
  print(f4)
  time.sleep(fps)
  clear()
  print(f5)
  time.sleep(fps)
  clear()
  
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
play(.3)
