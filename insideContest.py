
STUDENT_ID = 2
FACULTY_NAME = -1
STUDENT_VOTE = 3
STAFF_SCORE = 20
STAFF_VOTE = 2
OTHER_FACULTY_PROGRAMS = 3


def inside_contest(faculty, file_name):
    facultyPrograms = creatFacultyProgramsList(faculty, file_name)
    file_name = open(file_name, 'r')
    votersIds = []
    for line in file_name:
        programNameVote = line.split()
        if programNameVote[0] == "inside" and programNameVote[1] == "contest":
            if programNameVote[STUDENT_ID] in votersIds or programNameVote[FACULTY_NAME] != faculty:
                continue
            votersIds.append(programNameVote[STUDENT_ID])
            for iterator in facultyPrograms:
                if programNameVote[STUDENT_VOTE] == iterator[0]:
                    iterator[1] += 1
    print(facultyPrograms)
    name = findWinnerProgram(facultyPrograms)
    return name


def creatFacultyProgramsList(faculty, file_name):
    file_name = open(file_name, 'r')
    facultyPrograms = []
    for line in file_name:
        programName = line.split()
        if programName[0] == "staff" and programName[1] == "choice":
            if programName[FACULTY_NAME] == faculty:
                lineLength = len(programName)
                facultyPrograms.append([programName[STAFF_VOTE], STAFF_SCORE])
                for i in range(OTHER_FACULTY_PROGRAMS, lineLength - 1):
                    facultyPrograms.append([programName[i], 0])
                break
    file_name.close()
    return facultyPrograms


def findWinnerProgram(faculty_programs):
    maximum = -1
    name = " "
    for index in faculty_programs:
        if index[1] > maximum:
            maximum = index[1]
            name = index[0]

    return name


def main():

    print(str(inside_contest("cs", "test.txt")))



if __name__ == '__main__':
    main()
