class Student():

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