# Create constructor and objects of class college

class College:
    def __init__(self, name, student_count , univercity):
        print(f"College constructor is running for {name}")
        self.name = name
        self.student_count = student_count
        self.univercity = univercity

college1 = College("City College", 1200 , "Shivaji Univercity")
college2 = College("National College", 1800 , "Shivaji Univercity")

print(college1.student_count)

college1.student_count = 1400

print(college1.student_count)
print(college2.univercity)