import numpy as np
import pickle 

model = pickle.load(open("C:/xampp/htdocs/CG/careerlast.pkl", 'rb'))

print("Rate your efficieny in different subjects (1-7) : ")
arr = []
arr.append(int(input('Database Fundamentals: ')))
arr.append(int(input('Computer Architecture: ')))
arr.append(int(input('Distributed Computing Systems: ')))
arr.append(int(input('Cyber Security: ')))
arr.append(int(input('Networking: ')))
arr.append(int(input('Development: ')))
arr.append(int(input('Programming Skills: ')))
arr.append(int(input('Project Management: ')))
arr.append(int(input('Computer Forensics Fundamentals: ')))
arr.append(int(input('Technical Communication: ')))
arr.append(int(input('AI ML: ')))
arr.append(int(input('System engineer: ')))
arr.append(int(input('Business Analysis: ')))
arr.append(int(input('Communication skills: ')))
arr.append(int(input('Data Science: ')))
arr.append(int(input('Troubleshooting skills: ')))
arr.append(int(input('Graphics Designing: ')))
print()
# Convert list into numpy array
arr = np.array(arr)
print("Numpy array: ", arr)

# Tranpose of matrix
arr = arr.reshape(1,-1)
print("Reshape array: ", arr)

# Convert into boolean matrix (if there is sligest probabilty that a point blongs to certain class write true else false)
pred = model.predict_proba(arr)
pred = pred > 0.05
print(pred)

#Create dictionary for those whose voolean value is true dict as { index : index whose value is true in pred }
i = 0
j = 0
index = 0
res = {}
while j < 17:
    if pred[i, j]:
        print(i, j ,index)
        #res[index] = j
        print(res)
        #print()
        index += 1
    j += 1

print("Final result: ", res)

predictions = model.predict(arr)
print("Main result: ", predictions[0])

jobs_dict = {0:'AI ML Specialist',
                   1:'API Integration Specialist',
                   2:'Application Support Engineer',
                   3:'Business Analyst',
                   4:'Customer Service Executive',
                   5:'Cyber Security Specialist',
                   6:'Data Scientist',
                   7:'Database Administrator',
                   8:'Graphics Designer',
                   9:'Hardware Engineer',
                   10:'Helpdesk Engineer',
                   11:'Information Security Specialist',
                   12:'Networking Engineer',
                   13:'Project Manager',
                   14:'Software Developer',
                   15:'Software Tester',
                   16:'Technical Writer'}

# Different job roles suitable 

print("Different job roles you can persue: ")
print()
print(1, predictions[0])

index = 2
for key,value in res.items():
    if predictions[0] != jobs_dict[value]:
        print(index, jobs_dict[value])
        index += 1

