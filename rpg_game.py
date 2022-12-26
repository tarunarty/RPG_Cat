import random
import turtle
import tkinter



def options(lis,A):
    v = []
    
    for i in range(len(lis[A])):
        if lis[A][i]:
            v.append(i)

    return v




#setup

story = ["You wake up and stretch from your front paws all the way to the tip of your tail. After displaying the nonchalant grace of a feline, you look at the afternoon sky and muse where you will go from here.",
         "Having walked a moderate amount, you find yourself at the edge of the forest. You gaze both at the climbable trees ahead as well as the lollygagging humans behind, deciding what to do.",
         "Amidst the life of the city, you find yourself surrounded by chases and the movement of slow giants. A particular noise in the distance reaches your ears and amuses you.",
         "Having nothing particular to do, you end up in the marketplace. With food kept atrociously close to fire as well as pesky humans blocking you, it wasn’t the friendliest place, but it would do.",
         "Roaming around the vicinity, you find a shiny treasure on the tempered stone. Nudging it with your nose leads to a pleasant sound; it even makes you smile.",
         "You stand in front of the granny’s abode, a mystical being that always carried food. Expectations of tasty treats did not deter you from seeing an unwitting mouse in the distance.",
         "Happy with your bell, you took it and wondered whether to show it to your friends now or later.",
         "Life Is strange sometimes; you lose something yet end up finding something else. You happily nibble on newly acquired fish, your tail dancing like grass in the wind. In the corner of your eyes, you notice some movement.",
         "Alas, it turned out that the mouse wasn’t exciting enough to be captured. The thrill is in the chase, not the catch, you remind yourself, and look around hollow places the likes you don’t frequent.", 
         "Just as you approach your clowder, all heads turn at the nearby annoying mewlings of a human baby. You roll your eyes but see half of your kin approach the source of irritation still.",
         "Roaming around the forest still, you see the sun beginning to set and longer patches of shade for your paws forming. Close by; you see a horse forced to pull hefty loads behind it. Wanting to help the horse but uncaring enough to actually save them, you jump on it for a ride.",
         "After a brief discourse on life’s triviality, one of the remaining individuals of the clowder floated the prospect of paying a visit to the mouse theatre.",    
         "Hardly a surprise you find in front of yourself a prattling human kitten unable to fend for herself. Her mother looked frantic, unsure of whether to feed her or caress her.",
         "Noticing the terrain around, you notice familiar shapes as the carriage continues on its journey. Perhaps the carriage will stop at your town, perhaps later, perhaps not at all.",
         "Midway in the mice theatre’s performance was a scene starring stinky cheese. You often left at this part, and it just so happened that there was an open window nearby.",
         "You managed to bear yourself for the various stinky cheeses and finally saw the mouse being adopted and then running a restaurant. It was almost endearing.",
         "Closer inspection led to no results; the child still wept, and the mother still fretted. Having fulfilled your amusement, you…",
         "Hearing your treasure, the child has calmed down a little. You decide to leave the bell behind; there were those who would need it more. The mother has bent down and reaches with an open paw towards you, perhaps…",
         "The mother scratches you behind your ear for a second everything is not so pointless anymore",
         "You hop out to the terrace of a building and then move upwards to the top of a spire. From there, you look out at the sky and wish there were fewer clouds.",
         "You look around to see a new world of structures needlessly complex and winds of a different smell. In the distance, you could see a world of blue and were intrigued by what you could find inside.",
         "You head back to your usual spot, aware of the fact that nothing really beats the comfort of one’s own cardboard box. With a smaller stretch than before and a round or two of chasing your tail, you rest and drift off in slumber.",
         "You look around to chase the red ball of thread as it unravels. In the distance, the child - Era, they called her apparently - laughed heartily. Around your neck was a better treasure than before, though it still startled you sometimes. In the end, though, you knew that everything would be alright."]

storytree = [[[1, "Go to forest"],[2, "Go to city"],[3,"Do nothing"]],
             [[3, "Head towards humans"],[4, "Venture inside"]],
             [[3, "Follow the sound"],[5, "Ignore the noise"]],
             [[4, "Wander around"],[5, "Visit the friendly neighbourhood granny"]],
             [[6, "Take the bell with you"],[7, "Leave it behind"]],
             [[7,"Meow at the door"],[8,"Chase the mouse"]],
             [[9,"friends must know of my new toy!"],[10,"Friends can wait, forest it is"]],
             [[8,"chase the movement"],[9,"Eh, probably just some shadow, go to the hangout spot instead."]],
             [[12,"Roam around"]],
             [[10," ignore and move on with your day"],[11,"stay behind with the unmoving half"],[12,"satiate curiosity, knowing well enough its myth"]],
             [[13,"Jump on the carriage"]],
             [[14,"Time to see some mice dance"],[16,"Enough rodents for the day"]],
             [[16,"approach them"],[17,"approach them with bell"]],
             [[19,"hop off the carriage into the familiar"],[20,"remain seated for the unknown destination."]],
             [[15,"Bear through the smell and see how the theatre ends"],[19," Leap out into the night sky"]],
             [[21,"Satisfied for the time being, you…"]],
             [[21,"..."]],
             [[18,"go over to the mother"],[21,"meow once and then leave"]],
             [[22,"..."]],
             [[21,"You head back down, satisfied, you"]],
             [], [], []]

storyline =[[0 for __ in range(23)] for ___ in range(23)]
for line in range(22):
    for x in storytree[line]:
        a,b = x[0],x[1]
        storyline[line][a] = b



#primary
#start playing and ending circuit seperate initialisation
print("You are a cat (press -1 to quit playing)")
path = []
end_flag = 0
current = 0

while True:
    
    path.append(current)
    print()
    print(story[current])
    print()

    op = options(storyline,current)
    #exceptions
    if not storytree[current]:
        print()
        print("You have reached the END!! Thank you for playing.")  
        break
    if current==12 and 6 not in path:
        op = op[:1]
        
    for o in range(len(op)):
        print(o+1,"-",storytree[current][o][1])

    choice = int(input("Choose an option: "))
    
    if choice==-1:
        end_flag = 1
        break
    if choice not in [xx for xx in range(1,len(op)+1)]:
        print("Choose one of the options please.")  
        continue
    
    current = op[choice-1]


if end_flag == 1:
    print("Thank you for playing!")




"""
#GUI Experiments
root = tkinter.Tk()

root.title("NAME OF NEKO GAME")

root.geometry("1125x600")
  

instructions = tkinter.Label(root, text = "Type in the number correspoding to the option you want to pursue",font = ('Helvetica', 12))
instructions.pack() 
  

scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('Helvetica', 12))    


e = tkinter.Entry(root)
  
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
  
# set focus on the entry box
e.focus_set()
  
# start the GUI
root.mainloop()

"""




    
    
    
