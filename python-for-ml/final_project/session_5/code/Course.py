class Course:
    _id_counter = 1

    def __init__(self, name):
        self.course_id=Course._id_counter
        Course._id_counter +=1
        self.name=name
        self.enrolle_students=[]
    
    def __repr__(self):
        return f"course ID: {self.course_id}, Name: {self.name}, Enrolled: {len(self.enrolle_students)}"
    def enrolled_student(self, student):
        if student not in self.enrolle_students:
            self.enrolle_students.append(student)
            print("student enrooled succesfully")
        else:
            print("student already enrooled")
    def remove_student(self, student):
        if student in self.enrolle_students:
            self.enrolle_students.remove(student)
            print("student removed succesfully")
        else:
            print("student not found in course")
        

