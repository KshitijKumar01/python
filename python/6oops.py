print(type("sfsd"))

#creating the class
class test:
    pass
a = test()
print(type(a))


# self keyword is used to bind the function to the class
class pwskilss:
    def welcome_msg(self):
        print("Welcome to pw skills")
rohan = pwskilss()
rohan.welcome_msg()


class pwskills1():

    #constructor
    def __init__(self, phone_num, email_id, student_id):
        self.phone_num = phone_num
        self.email_id = email_id
        self.student_id = student_id

    def return_student_details(self):
        return self.student_id, self.phone_num, self.email_id
    

rohan = pwskills1(1213, "kshitij@gmail.com", "20BCS4094")
print(rohan.return_student_details())



