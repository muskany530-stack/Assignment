'''
while True :
      print("========== ESCAPE ROOM MYSTERY GAME =========== ")
      print("1. Start the Game")
      print("2. Rules")
      print("3. EXIT")

      options= int(input("Enter your choice :"))
      lives =3
      score =0
      game_over =False
      match options :
            

            case 1:
                  room1_clear = False
                  room2_clear = False
                  room3_clear = False

                  name = input("Enter your name :")
                  print("Welcome {}❤ !!".format(name))
                  print("Lives =", lives)
                  print("Score =", score)

                  print("=============== You entered ROOM 1 ===============")
                  lives = 3
                  score =0
                  
                  while lives>0 :
                        print("Choose a Door to escape :")
                        print("1. Red Door")
                        print("2. Blue Door")
                        print("3. Green Door")
                        
                        Door=int(input("Which Door??"))
                        
                        match Door:
                              case 1 :
                                    print("Oops! A trap. You lost 1 life.")
                                    lives = lives - 1   
                                    room1_clear= False                             
                                    
                                     
                              case 2 :
                                    print("Great! you found the correct Door.")
                                    print("You found a Gem💎")
                                    print("Score Points  =", score+10)
                                    print("Moving to ROOM 2...")
                                    print("Lives left =",lives)
                                    room1_clear =True
                                    break
                              case 3:
                                    print("Wrong door! You fell into a pit.")
                                    lives = lives - 1 
                                    room1_clear= False
                              case __ :
                                    print("Invalid door")               
                        
                        
                        print("Lives left =",lives) 
                        if  lives == 0 :
                                print("Bhai mar gya tu")
                                print("Game end")
                                break
                        
                  if room1_clear==True :
                    
                    for i in range(1,lives+1):
                        print("=============== You entered ROOM 2 ===============")
                        print("Answer the Logical question...")
                        ques = input("The more you take , the more you leave behind. WHO AM I ??🤔 ").lower()
                        if ques == "footprint" :
                           room2_clear=True
                           print("Congratulations you crossed the level !!")
                           print("score Points =",score+20)
                           break
                           
                        else :
                           lives = lives -1
                           room2_clear =False
                           print("You lost live..  lives =",lives)
                           

                    print("Lives left =",lives) 
                    if  lives == 0 :
                            print("Bhai mar gya tu")
                            print("Game end")
                            break

                  if room2_clear ==True :
                    
                    for j in range(1,lives+1):
                       print("=============== You Entered ROOM 3 ===============")
                       print("Solve the Riddles To Escape.")
                       riddle1 =input("A Bottle contains water. How can you make it empty without Pouring , Drinking , or breaking it ?").lower()
                       riddle2=input("What has many teeths but cannot bite ?").lower()
                       if riddle1 == "evaporate the water" and riddle2== "comb":
                           room3_clear =True
                           print("score Points =",score+40)
                           print("Great!! , The ESCAPE path is nearby...💥 ")
                           break
                           
                       else:
                           lives = lives -1
                           room3_clear =False
                           print("You lost live..  lives =" ,lives)

                    print("Lives left =",lives) 
                    if  lives == 0 :
                        print("Bhai mar gya tu")
                        print("Game end")
                        break

                  if room3_clear ==True :
                    print("=============== You Entered the KEY ROOM ===============g")
                    print("You found a chest box on the Table , with the three keys kept in the drawer.🗝 ")
                    print("----THE KEY TO ESCAPE THE ROOM IS IN THE CHEST BOX ----")

                    print("Silver key")
                    print("Golden key")
                    print("Bronze key")

                    print("""The clue to open the chest :
                        the old wizard whispered...
                                The key you seek shine like the 🌞, but remember.. appearance can deceive.""")
                    
                    key= input("Select a key to open the Treasure che$t").lower()
                    match key :
                            case "silver key":
                                  print("Damn! , A snake bite you")
                                  print("THANK YOU FOR PLAYING I HOPE U ENJOYED!! 🤩 ") 
                                  lives = lives -1
                                  
                            case "golden key":
                                  print("BOOYAH !!🎉, the Castle Door Opened you can escape now.")
                                  print("Score Points =",score+80)

                            case "bronze key":
                                  print("You are Trapped in the castle forever ☠.") 
                                  print("THANK YOU FOR PLAYING I HOPE U ENJOYED!! 🤩 ") 
                                  lives = lives -1
                                  break
                            case __ :
                                  print("invalid key")  
                                  break  
                    print("Lives left =",lives) 
                    game_over=True

            case 2:
                print("\n========== GAME RULES ==========")
                print("Welcome to the Escape Room!")
                print("Your mission is to escape the mysterious castle by solving puzzles and making the right choices.")
                print("1. You have 3 lives at the start of the game.")
                print("2. Choose the correct door to move to the next room.")
                print("3. Every wrong choice or wrong answer costs 1 life.")
                print("4. Solve puzzles and riddles to unlock the next room.")
                print("5. Collect gems to increase your score.")
                print("6. If your lives become 0, the game is over.")
                print("7. Read every clue carefully before answering.")
                print("8. In the final room, choose the correct key to escape.")
                print("9. Reach the exit with at least 1 life to win the game.")
                print("10. Have fun and think before you choose!")
                print("Good Luck! ")
                print("=================================\n")
                continue

            case 3:
                print("Thank you for playing Escape Room Mystery Game!!!")
                print("Game existed..")
                break
      if game_over==True or room3_clear==True :

        again= input("Do you want to play again ?(YES/NO) : ").lower()
        match again:
            case "yes" :
               continue 
            case "no" :
               print("Thank you.. Hope u enjoyed!")
               break  
            case __ :
               print("Please enter correct option (Yes/No) : ")
               break
'''

            
            

      

                
      
       
                           
                       
                  
                       
                       
                       


 
                        
                      
