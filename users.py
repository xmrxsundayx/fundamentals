class user:
    def __init__(self, first_name, last_name, email, age, member, points):
        self.first_name =first_name
        self.last_name =last_name
        self.email =email
        self.age =age
        self.member =member
        self.points =points

#Have this method print all of the users' details on separate lines.
    def print_user_info(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.member}\n{self.points}")
        return self

#Have this method change the user's member status to True and set their gold card points to 200.
    def member_status(self):
        if self.member == True:
            print("you are already a member!")
        elif self.member ==False:
            self.member, self.points = True,200
            print(f"Congrats, You are a new member! \nYou received {self.points} sign up bonus points")
            return self

#have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if self.points < amount:
            print(f"Sorry, you do not have enough points. {self.points}")
        elif self.points >= amount:
            self.points = self.points - amount
            print(f"Thank you for you purchase. You have {self.points} left.")
        return self



user1 = user("Jack", "Sparrow", "blackpearl@parlay.com", "45", True, 150)
user2 = user("Will", "Turner", "iloveelizabeth@palray.com", "28", False, 120)
user3 = user("Black", "Beard", "deathtocaptainjacksparrow@parlay.com", "50", True, 20)

user1.print_user_info()
user1.member_status()
user1.spend_points(50)
user2.print_user_info()
user2.member_status()
user2.spend_points(50)
user3.print_user_info()
user3.member_status()
user3.spend_points(50)