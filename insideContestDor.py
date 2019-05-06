

def inside_contest(faculty, file_name):
    file = open(file_name, 'r')
    faculty_programs = []
    for line in file_name:
        line = file.readline()   #string - one line from the file 'test.txt'
        list = line.split()
        if list[0] == "staff" and list[1] == "choice":
            if list[-1] == faculty:
                for i in range(2, len(list)-1):
                    faculty_programs.append([list[i], 0])
                break
    file.close()
    return faculty_programs
    #return [1,4,5]


def main():
    print(inside_contest("cs", "test.txt"))
    #dorList = [1,2,3]
    #print(dorList)


if __name__ == '__main__':
    main()
