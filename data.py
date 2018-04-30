N_Days = 3
N_Time = 3
N_Profs = 3
N_Courses = 5
N_Rooms = 4

RoomTime = [[0,1,0],[1,1,1],[1,1,0],[1,1,1]]
Prof = [[1,1,0],[1,0,0],[1,1,1]]
CourseProf = [0,0,1,2,2]
Clash = [[False]*N_Courses]*N_Courses
CourseClasses = [2,1,2,1,2]


# Clash due to students
Clash[0][2] = Clash[2][0] = True

# Clash due to same faculty
for i in range(N_Courses):
    for j in range(i+1,N_Courses):
        if CourseProf[i]==CourseProf[j]:
            Clash[i][j] = Clash[j][i] = True

# Additional checks for validity:
totalTime = sum([av for day in RoomTime for av in day])
assert(sum(CourseClasses)<=totalTime)
