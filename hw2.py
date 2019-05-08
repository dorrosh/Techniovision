#STUDENT_ID = 2
#FACULTY_NAME = -1
#STUDENT_VOTE = 3
#STAFF_SCORE = 20
#STAFF_VOTE = 2
#OTHER_FACULTY_PROGRAMS = 3
#STUDENT_ID_VOTE = 1

import Techniovision


def inside_contest(faculty, file_name):
    facultyPrograms = creatFacultyProgramsList(faculty, file_name)
    file_name = open(file_name, 'r')
    votersIds = []
    for line in file_name:
        programNameVote = line.split()
        if programNameVote[0] == "inside" and programNameVote[1] == "contest":
            if programNameVote[2] in votersIds or programNameVote[-1] != faculty:
                continue
            votersIds.append(programNameVote[2])
            for iterator in facultyPrograms:
                if programNameVote[3] == iterator[0]:
                    iterator[1] += 1
    name = findWinnerProgram(facultyPrograms)
    return name


def creatFacultyProgramsList(faculty, file_name):
    file_name = open(file_name, 'r')
    facultyPrograms = []
    for line in file_name:
        programName = line.split()
        if programName[0] == "staff" and programName[1] == "choice":
            if programName[-1] == faculty:
                lineLength = len(programName)
                facultyPrograms.append([programName[2], 20])
                for i in range(3, lineLength - 1):
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


def runTechniovision(file_name):
    techniovision = []
    position = 0
    input_file = open(file_name, 'r')
    for line in input_file:
        programNameVote = line.split()
        if programNameVote[0] == "staff" and programNameVote[1] == "choice":
            faculty = programNameVote[-1]
            input_file.close()
            techniovision.append([faculty, inside_contest(faculty, file_name)])
            input_file = open(file_name, 'r')
            input_file.seek(position)
        input_file = open(file_name, 'r')
    input_file = open(file_name, 'r')
    studentsId = []
    t = Techniovision.TechniovisionCreate()
    for line in input_file:
        lineString = line.split()
        if lineString[0] == "techniovision":
            if lineString[1] not in studentsId:
                studentsId.append(lineString[1])
                for index in techniovision:
                    if index[1] == lineString[2]:
                        Techniovision.TechniovisionStudentVotes(t, int(lineString[1]),
                                                                str(lineString[-1]), str(index[0]))
                        break
    Techniovision.TechniovisionWinningFaculty(t)
    Techniovision.TechniovisionDestroy(t)


def main():
    runTechniovision("test.txt")


if __name__ == '__main__':
    main()
