import random

def time_passes():        
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def start_fight():
      text = '''
              .:-===-.
            =#@@%%%%##+:
   ..     -%@@@%%%%##***+:
   ##+.  -%%%%#%######***+-     -++.
  =#%%#- %%#++=*%##+=++***+=   *##*=.
   -###*-%%=-+**#***++=+**+=- =#++-.
    -%***%%*+******+*****++=---===
    :@#**#%*#+--=*+.:-::==-=--=--:
     +%#*#%+---:==*:::::-+=====--
      +==#%#*+==*****+++++======-.
       ##%#******+++++++======----:.
     =#%#***+++++++==+++========---::
 ..=#####***+++=========--------::::::
 .:+==+==***++++++==---------:::::::::.
         ........::.  .       ...  .
'''

      print(text)
      

time_passes()
playerName = input("What's your name adventurer? ")
print(f"\nA great adventurer, {playerName} is lost in the fortress of darkness, amidst its slimy walls and disgusting odor.\n")

print(f"The great adventurer, {playerName} is faced with only two options:\n"
      "1) Try to climb out of it\n"
      "2) Wait for help to come\n")
choice01 = int(input())
rand1 = random.randint(0, 1)

time_passes()
if choice01 == 1:
    print(f"\n{playerName} starts to climb the slimy walls of the fortress,\n" 
          "grabbing onto any ledge they can find,\n"
          "the task is proving to be difficult.\n")
    print(playerName, " slips on a slippery tile.")
    if rand1 == 1:
        print(f"{playerName} musters up all their strength and swings themselves to a nearby tile.")
    else:
        print(f"{playerName} falls to their doom.")
        exit()
else:
    print(f"\n{playerName} waits and waits, and waits, and waits, and waits,\n" +
          "and waits, and waits, and waits, and waits, and waits\n" +
          "and nobody comes.")
    exit()
time_passes()
print(f"\n{playerName} finally comes to the top of the inside of the fortress,\n"
      "seeing a wooden door on the ceiling, they open it. Only to see\n" 
      "that there's a whole new room with larger height and width than anything\n"
      "that could be supported by the walls of the fortress they just cleared.")

time_passes()

print(f"\nExploring this wasteland {playerName} starts to understand that this isn't a room.\n"
      "This is a whole new world without any walls, nothing just the pavement\n"
      "beneath your feet and the ominous dark sky, no ceiling in sight.\n"
      f"{playerName} finds a shabby old sword and a few throwing knives.")

print("\nSuddenly you are ambushed by a group of low-life slime, what do you do:\n"
      "1) Fight\n"
      "2) Flee")
choice02 = int(input())


if choice02 == 1:
      start_fight()
      SlimeHP=15
      while SlimeHP>=0:
            SwordAttack= random.randint(5,9)
            ThrowingKnife= random.randint(1,3)
            print('\n' "What wepon will you use:\n"
                  "1) Sword\n"
                  "2) Throwing Knives\n")
            choice03=int(input())
            if choice03==1:
                  SlimeHP-=SwordAttack
                  print(f"The low life slime took {SwordAttack} demage.")
            elif choice03==2:
                  SlimeHP-=5
                  if ThrowingKnife>=2:
                        print("The low life slime was hit by the throwing knives and took 5 demage.")
                  else:
                        print(f"{playerName} missed the slime!")
      print(f"{playerName} defeated the slime!")
elif choice02==2:
      print("The slime are surprislinglly swift and check up to the hero devouring them.")