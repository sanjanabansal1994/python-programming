# tee ratkaisusi tänne
class Course:
    def __init__(self, name):
        self.name= name
        self.grade= []
        self.credit = 0

    def add_grade(self, grade):
        self.grade.append(int(grade))
    
    def add_credit(self, credit):
        self.credit= int(credit)

class CourseApp:
    def __init__(self):
        self.courses={}
    
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name= input("name: ")
        grade= input("grade: ")
        credit = input("credits: ")
        if not name in self.courses:
            self.courses[name]= Course(name)
        self.courses[name].add_grade(grade)
        self.courses[name].add_credit(credit)


    def get_course_data(self):
        name= input("name: ")
        if name in self.courses:
            print(f'{name} ({self.courses[name].credit} cr) grade {max(self.courses[name].grade)}')
        else:
            print("no entry for this course")

    def get_stat(self):
        final_grade=[]
        total_credit=0
        for values in self.courses.values():
            final_grade.append(max(values.grade))
            total_credit+=values.credit
        print(f"{len(self.courses)} completed courses, a total of {total_credit} credits")
        print(f'mean {sum(final_grade)/len(self.courses):.1f}')
        print("grade distribution")
        for i in range(5,0,-1):
            x_str= 'x'*final_grade.count(i)
            print(f'{i}: {x_str}')


    def execute(self):
        self.help()
        while True:
            command= input("command: ")
            if command=="0":
                break
            if command=="1":
                self.add_course()
            if command=="2":
                self.get_course_data()
            if command=="3":
                self.get_stat()
                

# if __name__=="__main__":
app = CourseApp()
app.execute()     
