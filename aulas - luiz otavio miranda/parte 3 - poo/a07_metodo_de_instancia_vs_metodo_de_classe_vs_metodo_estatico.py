class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

x1 = Connection()
x1.set_user('alv')
x1.set_password(12345)

print(x1.host)
print(x1.user)
print(x1.password)

print()

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    @classmethod
    def set_user_and_password(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password

        return connection

x1 = Connection.set_user_and_password('alv4', 123456)

print(x1.host)
print(x1.user)
print(x1.password)

print()

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    @staticmethod
    def log(message):
        return 'Log ->', message

x1 = Connection.log('oi!')

print(*x1)
