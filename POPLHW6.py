def sor(y):
    if(y[1][2] == "E"):
        return y[1][3] + .1
    else:
        return y[1][3]

idNumList = []
gradeList = []
sortGL = []
firstNameList = []
lastNameList = []
eagerList = []
finalGradeList = []

x = int()
idcheck = int()
# opening the text file
with open('studentInfo.txt','r') as file:
    # reading each line
    for line in file:
        # reading each word
        for word in line.split():
            if idcheck == 0:
                x = 0

            if word.isnumeric():
                #Check for IDNums
                if(len(word) > 3):
                   idNumList.append(word)  
                   idcheck = 1
                else:
                   gradeList.append(int(word))

            if idcheck == 1:
                x = x + 1 
            if x == 2:
                firstNameList.append(word)
            if x == 3:
                lastNameList.append(word)
            if x == 5:
                eagerList.append(word)
                idcheck = 0
    #print(idNumList)
    #print(gradeList)
    #print(firstNameList)
    #print(lastNameList)
    #print(eagerList)
    
students = {}

for i in range(len(idNumList)):
    students[idNumList[i]] = [firstNameList[i], lastNameList[i],eagerList[i], gradeList[i]]

students = dict(sorted(students.items(),key=sor,reverse=True))

NUM_STUDENTS = len(idNumList)
count = int()
for key, value in students.items():
    if (count > (NUM_STUDENTS - (NUM_STUDENTS / 10)) - 1):
        students[key][2] = 'F'
        finalGradeList.append('F')
        break
    if (count < (NUM_STUDENTS / 3) - 1):
        finalGradeList.append('A') 
        students[key][2] = 'A'
    elif (count < (2 * NUM_STUDENTS / 3) - 1):
        finalGradeList.append('B') 
        students[key][2] = 'B'
    elif (value[2] == 'E'):
        finalGradeList.append('C') 
        students[key][2] = 'C'
    else:
        finalGradeList.append('D') 
        students[key][2] = 'D'
     
    count = count +1
print(students)
print(finalGradeList)



#Html FILE
f = open('popl6EthanTillotson.html', 'w') 
  
# the html code which will go in the file GFG.html 
html_template = """<html> 
<head> 
    <style> 
        body { 
            text-align: center; 
        } 
  
        h1 { 
            color: green; 
        } 
  
        th { 
            color: black; 
        } 
  
        table, 
        tbody, 
        td { 
            border: 1px solid black; 
            border-collapse: collapse; 
        } 
    </style> 
</head> 
<body> 
    <center> 
        <table> 
            <thead> 
              
            </thead> 
            <tbody> 
                <tr> 
                    
                </tr> 
                <tr> 
                   
                </tr> 
            </tbody> 
        </table> 
    </center> 
</body> 
  
</html>    
"""
# writing the code into the file 
f.write(html_template) 
# close the file 
html = '<table>'

for i in range(NUM_STUDENTS):
    html += "<tr>" + "<td>" + idNumList[i] + "</td>" + "<td>" + firstNameList[i] + "</td>" + "<td>" + lastNameList[i] + "</td>" + "<td>" + students[idNumList[i]][2]  + "</td>" + "</tr>"

html += "</table>"

f.write(html)
f.close() 