import random;moves=['rock','paper','scissors'];bw=0;pw=0;a=0;b=random.randint(0,2);a=input('move?: ');ab=0 if a=="rock" else 1 if a!="scissors" else 2;c=(3+ab-b)%3;print('Bot Move:{}'.format(moves[b]));print("win" if c==1 else "lose" if c!=0 else "tie")
#print("win"if input('>')!=__import__('random').choice(['rock','paper','scissors'])else"lose") Kinda works but could be made better HMMM
