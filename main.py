from cat import Cat

print("""Welcome to my cat Game!
           __..--''``---....___   _..._    __
 /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // / 
///_.-' _..--.'_    \                    `( ) ) // //
/ (_..-' // (< _     ;_..__               ; `' / ///
 / // // //  `-._,_)' // / ``--...____..-' /// / //
      
 /\_/\    ______
( o.o )  {Hello!}
 > ^ <  -      """)
name=input("Enter Cat name: ")
colour=input("Enter Cat colour: ")
my_cat=Cat(name,colour)
while True:
    action=input("""
RULES: Make sure your cat's energy doesn't get to less than 5!
       Also make sure your cat's weight doesn't get to less than 5!
       And make sure your cat doesn't get too fat, so it can't be heavier than 30!
       After your cat reaches 20, it will die of old age:(
What would you like to do?
1.Train
2.Feed
3.Play
4.Sleep
5.See stats
""")
    
    if action=="1":
        my_cat.train()
        value=my_cat.check()
        if value==False:
            print("Your cat died because it's energy is too low to train :(")
            break
    elif action=="2":
        my_cat.feed()
        if value==False:
            print("Your cat died :(")
            break            
    elif action=="3":
        my_cat.play()
        if value==False:
            print("Your cat died because it's too too tired :(")
            break        
    elif action=="4":
        my_cat.sleep()
        if value==False:
            print("Your cat died :(")
            break        
    elif action=="5":
        my_cat.stats()
    

