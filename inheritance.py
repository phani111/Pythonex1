class Parent():
    def __init__(self,last_name,eye_color):
        print("parent construcot called")
        self.last_name = last_name
        self.eye_color = eye_color


    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)


class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys


#billy_cyrus = Parent("Cyrus","blue")
#billy_cyrus.show_info()
milley_cyrus = Child("Cyrus","Blue",5)
milley_cyrus.show_info()

        
