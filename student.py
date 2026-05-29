class Student:
    def attend_class(self):
        print("Attending classes")

class Teacher:
    def teach_lab(self):
        print("Teaching lab sessions")

class TeachingAssistant(Student, Teacher):
    def details(self, name):
        print("Teaching Assistant:", name)

ta = TeachingAssistant()

ta.details("Durga")
ta.attend_class()
ta.teach_lab()