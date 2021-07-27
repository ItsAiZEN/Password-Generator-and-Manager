import random
import string


class Password:

    def __init__(self, name, username='', password='', website='', ):
        self.name = name
        self.username = username
        self.password = password
        self.website = website

    def __str__(self):
        return f'Name: {self.name} \nUsername: {self.username} \nPassword: {self.password}\nWebsite: {self.website}'

    @staticmethod
    def generate_password(length=8, numbers='T', letters='T', capital_letters='F', symbols='F'):
        characters = ''
        if numbers == 1:
            characters += string.digits
        if letters == 1:
            characters += string.ascii_lowercase
        if capital_letters == 1:
            characters += string.ascii_uppercase
        if symbols == 1:
            characters += '!@#$%^&*()_+-='
        random_password = random.choices(characters, k=length)
        random_password = ''.join(random_password)
        return random_password
