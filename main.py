from cat import Cat

print("Welcome to my cat Game!")
name=input("Enter Cat name: ")
colour=input("Enter Cat colour; ")
my_cat=Cat(name,colour)
while True:
    action=input("""
What would you like to do?
1.Train
2.Feed
3.Play
4.Sleep
5.See stats
""")
    if action=="1":
        my_cat.train()
    elif action=="2":
        my_cat.feed()
    

