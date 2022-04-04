import time
import sys
import itertools
import threading

#Meetings xD
print("Hii, What's your name ?")
name = input("=> ")
print("Hey", name+", What's the problem you are facing ?")
problem = input("=> ")

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rAnalysing Problem   ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
        #Get ready to be amazed !
    sys.stdout.write('\n\n\rCure found!                 ')
    print("\nCopy the link and Paste in a browser --> https://bit.ly/35AjlDS")

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True

