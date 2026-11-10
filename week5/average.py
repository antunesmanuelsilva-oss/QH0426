def student_marks(marks ):
    average = sum(marks)/len(marks)
    return average

mark_list = list(map(int,input('Enter marks separeted by space').split()))

average = student_marks(mark_list)
print('The average of the marks is',student_marks(mark_list))