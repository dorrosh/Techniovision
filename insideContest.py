import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
STUDENT_ID = 2
FACULTY_NAME = -1
STUDENT_VOTE = 3
STAFF_VOTE = 20
FIRST_STAFF_VOTE = 2
OTHER_FACULTY_PROGRAMS = 3


def inside_contest(faculty, file_name):
    faculty_programs = creatFacultyProgramsList(faculty, file_name)
    file_name = open(file_name, 'r')
    votersIds = []
    for line in file_name:
        programs_name_vote = line.split()
        if programs_name_vote[0] == "inside" and programs_name_vote[1] == "contest":
            if programs_name_vote[STUDENT_ID] in votersIds or programs_name_vote[FACULTY_NAME] != faculty:
                continue
            votersIds.append(programs_name_vote[STUDENT_ID])
            for iterator in faculty_programs:
                if programs_name_vote[STUDENT_VOTE] == iterator[0]:
                    iterator[1] += 1
    print(faculty_programs)
    name = findWinnerProgram(faculty_programs)
    return name


def creatFacultyProgramsList(faculty, file_name):
    file_name = open(file_name, 'r')
    faculty_programs = []
    for line in file_name:
        programs_name = line.split()
        if programs_name[0] == "staff" and programs_name[1] == "choice":
            if programs_name[FACULTY_NAME] == faculty:
                len1 = len(programs_name)
                faculty_programs.append([programs_name[FIRST_STAFF_VOTE], STAFF_VOTE])
                for i in range(OTHER_FACULTY_PROGRAMS, len1 - 1):
                    faculty_programs.append([programs_name[i], 0])
                break
    file_name.close()
    return faculty_programs


def findWinnerProgram(faculty_programs):
    maximum = -1
    name = " "
    for index in faculty_programs:
        if index[1] > maximum:
            maximum = index[1]
            name = index[0]

    return name


def main():
    my_file = os.path.join(THIS_FOLDER, 'test.txt')
    print(str(inside_contest("cs", my_file)))


if __name__ == '__main__':
    main()
