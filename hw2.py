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
            if programNameVote[2] in votersIds or \
               programNameVote[-1] != faculty:
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
    contestList = []
    position = 0
    inputFile = open(file_name, 'r')
    for line in inputFile:
        programNameVote = line.split()
        if programNameVote[0] == "staff" and programNameVote[1] == "choice":
            faculty = programNameVote[-1]
            inputFile.close()
            contestList.append([faculty, inside_contest(faculty, file_name)])
            inputFile = open(file_name, 'r')
            inputFile.seek(position)
        inputFile = open(file_name, 'r')
    inputFile = open(file_name, 'r')
    techniovision = Techniovision.TechniovisionCreate()
    for line in inputFile:
        lineString = line.split()
        if lineString[0] == "techniovision":
            for index in contestList:
                if index[1] == lineString[2]:
                    Techniovision.TechniovisionStudentVotes\
                    (techniovision, int(lineString[1]),\
                    str(lineString[-1]), str(index[0]))
                    break
    Techniovision.TechniovisionWinningFaculty(techniovision)
    Techniovision.TechniovisionDestroy(techniovision)


def main():
    runTechniovision("input.txt")


if __name__ == '__main__':
    main()
