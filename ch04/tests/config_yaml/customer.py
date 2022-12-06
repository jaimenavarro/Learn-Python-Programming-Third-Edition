class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return f'{self.name=} {self.email=}'


class Customers:
    def __init__(self, customers):
        self.list = list()
        for customer in customers:
            self.list.append((Customer(**customer)))




