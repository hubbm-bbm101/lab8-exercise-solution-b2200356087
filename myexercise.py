import sys
dicto = {}
inline=False
temporary_list = "a"
stuni = open(sys.argv[1], "r")
listo = stuni.readlines()
for line in listo :
    line.strip("\n")
students = sys.argv[2].split(",")
for student in students :
    inline=False
    try :
        for line in listo :
                if student in line :
                    inline = True
                    temporary_str = line.strip(student)
                    dicto[student] = temporary_str.strip(":")
                    print("Name: "+ student + ", University: " + dicto[student])
        if not inline :
            raise AssertionError

    except AssertionError :
            print("No record of ", student, "is found")
