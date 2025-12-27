# Here we are creating user class and relevant objects from it


class User:  # Parent class
    def __init__(self, id, fname, lname, email_id, role):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.email_id = email_id
        self.role = role


# fixed class for admin
class Admin(User):
    def __init__(self, id, fname, lname, email_id):
        super().__init__(id, fname, lname, email_id, role="Admin")
