
class User():
    def __init__(self, first_name, last_name, age, status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.login_attempts = 3
    def describe_user(self):
        print(self.first_name.title(),)
        print(self.last_name, )
        print(self.age)
        print(self.status)
        print(self.login_attempts)

    def increment_login_attempts(self, i):
        '''уыеличивает login_attempts на 1'''
        self.login_attempts += i

    def reset_login_attempts(self):
        '''обнуляте login_attempts'''
        self.login_attempts = 0
        print('должно обнулить')

    def greet_user(self):
        print('Hello', self.first_name.title())

user = User('yura', 'yankovski', '25', 'сложно')
#user.describe_user()
#user.greet_user()

user.reset_login_attempts() # все работает обнуляет
user.describe_user()
user.increment_login_attempts(1122) # добавили добовляет 1(1122)
user.describe_user()

#user2 = User('kolia', 'yankovski', '22', 'добре')
#user2.describe_user()
#user2.greet_user()

class Admin(User):
    def __init__(self,first_name, last_name, age, status ): #наслоедовал все атрибуты класса User
        super().__init__(first_name, last_name, age, status ) #  функцие совместили потомков и родителей
        self.privileges = ['разрешено добовлять сообщения', 'разрешено удалять пльзователйе', 'разрешено банить']

    def show_privileges(self):
        print('привилегии админу: ', self.privileges)

admin = Admin('yura', 'yanko', 25, 'fredom') # добавили аргументы но не выводили
admin.show_privileges()