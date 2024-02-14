"""
    Adicionar três métodos para comparar dois alunos
    1. Método para comparar "igualdade"
    2. Método para comparar "menor que"
    3. Método para comparar "maior que ou igual"
"""
import random

class Student():
    students = list()
    def __init__(self, name, age, number):
        """
            Para cada instância criada, é atribuído um nome e a quantidade de notas,
            todas as notas são inicialmente definidas como 0
        """
        
        self.name = name
        self.age = age
        self.score = []
        for n in range(number):
            self.score.append(0)
        Student.students.append(self)

    def studentsList(self):
        return self.students.append(self)

    def setName(self, newName):
        """Permite alterar o nome do aluno"""
        self.name = newName

    def getName(self):
        """Retorna o nome do aluno"""
        return self.name
    
    def setAge(self, newAge):
        """Permite alterar a idade do aluno"""
        self.age = newAge

    def getAge(self):
        """Retorna a idade do aluno"""
        return self.age

    def setScore(self, i, score):
        """Define o valor da nota do aluno, no índice informado"""
        self.score[i - 1] = score

    def getScore(self, i):
        """Retorna o valor da nota, no índice informado"""
        return self.score[i - 1]
    
    def getAverage(self):
        """Retorna a média das notas do aluno"""
        return sum(self.score) / len(self.score)
    
    def getHighScore(self):
        """Retorna a maior nota do aluno"""
        return max(self.score)
    
    def __str__(self):
        return "Name: " + self.name + "\nScores: " + self.score
    
    def isEqual(self, other):
        return True if self.name == other.name else False
    
    def isLessThan(self, other):
        return True if self.name < other.name else False
    
    def isGreaterThan(self, other):
        return True if self.name >= other.name else False



Student("Diogo", 26, 5)
Student("Josivaldo", 30, 5)
Student("Cariovaldo", 40, 5)
Student("Marilelza", 20, 5)
Student("Carol", 30, 5)

for student in Student.students:
    for i in range(5):
        s = random.randint(70, 100)
        student.setScore(i, s)
    print(f"Nome: {student.name} Idade: {student.age} Average: {student.getAverage()}")


# print("Igualdade: " + str(student1.isEqual(student2)))
# print("Menor que : " + str(student1.isLessThan(student2)))
# print("Maior ou igual que : " + str(student1.isGreaterThan(student2)))