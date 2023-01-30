class Person():  # classe genérica que terá classes herdeiras
    banana = 'banana da pessoa'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def class_name(self):
        print('Classe Pessoa')
        print(self.name, self.surname, self.__class__.__name__, '\n')

class Student(Person):  # classe que terá herdeiras passada nos parênteses
    def class_name(self):
        print('Classe Estudante')
        print(self.name, self.surname, self.__class__.__name__, '\n')

class Worker(Person):
    banana = 'banana do trabalhador'

student = Student('Ce', 'noura')
worker = Worker('Ce', 'bola')

student.class_name()
worker.class_name()

print('\n', Student.banana)
print(Worker.banana, '\n')

# ao buscar algo dentro de uma classe, caso ela faça parte de uma herança
# ela seguirá a ordem MRO (usar função help). Esse algo buscado vai ser
# retornado da primeira classe que o tiver.
help(Student)
