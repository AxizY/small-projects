import time
time.sleep(3)
f = open("pixeldata.txt", "r")
for x in f:
    for o in x:
        if o != "\n":
            playsound(f'{o}.wav')
            time.sleep(.75)
        else: time.sleep(1)
f.close()
