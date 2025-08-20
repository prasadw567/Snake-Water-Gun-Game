elements=["snake","water","gun"]

import random

choice_comp=(random.choice(elements))
print("Welcome to the Game","\nSNAKE,WATER,GUN")
input("Press Enter to start the game!!!")

while True:
    print("\n1:snake","2:water","3:gun")
    a=int(input("Enter your choice:"))
    user_choice=elements[a-1]
    if user_choice not in [1,2,3]:
        print("enter a vaild choice")
    
    def win():
     print(f"your choice:{user_choice}","           ",f"computer's choice:{choice_comp}")
     print("YOU WIN")
     input("press enter to proceed")
    def lose():
     print(f"your choice:{user_choice}","           ",f"computer's choice:{choice_comp}")
     print("try again!!!")
     input("press enter to proceed")

    if(choice_comp==user_choice):
        print(f"your choice:{user_choice}","           ",f"computer's choice:{choice_comp}")
        print("DRAW")
        input("press enter to proceed")
        
    else:
        match a:
            case 1:
                if(choice_comp==elements[1]):
                    win()
                else:
                    lose()
                
            case 2:
                if(choice_comp==elements[2]):
                    win()
                else:
                    lose()
                
            case 3:
                if(choice_comp==elements[1]):
                    win()
                else:
                    lose()
    play_again=input("Do you want to play again(y/n):")
    if(play_again=="n"):
        break
    












    
            


