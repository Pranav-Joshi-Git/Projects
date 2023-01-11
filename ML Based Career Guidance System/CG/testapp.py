from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route('/')
def career():
    return render_template("hometest.html")


@app.route('/predict',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      
      # Read form data 
      result = request.form
      data_file = open('data.txt', 'w')
      
      # convert form data to python dictionary
      res = result.to_dict(flat=True)
      data_file.write("\n\nForm Dictionary => " + str(res)+'\n')
      
      arr1 = res.values()
      arr = ([value for value in arr1])
      
      # Convert list into numpy array
      data = np.array(arr)
      data_file.write("\n\nNumpy Array => " + str(data)+'\n')

      # Tranpose of matrix
      data = data.reshape(1,-1)
      data_file.write("\n\nArray transpose => " + str(data)+'\n')
      
      # Load model and predict 
      loaded_model = pickle.load(open("careerlast.pkl", 'rb'))
      predictions = loaded_model.predict(data)      
      data_file.write("\n\nMain prediictions => " + str(predictions)+'\n')

      # Store form data in csv file (history.csv)
      hist = pd.DataFrame(data)
      hist.insert(17, 'Role', predictions[0], True)
      hist.to_csv('history.csv', mode='a', index=False, header=False)
      
      # Convert into boolean matrix (if there is sligest probabilty that a point blongs to certain class write true else false)
      pred = loaded_model.predict_proba(data)
      data_file.write("\n\nPrediction probabilty => " + str(pred)+'\n')      
      pred = pred > 0.05
      data_file.write("\n\nBoolean prediction => " + str(pred)+'\n') 
      
      #Create dictionary for those whose boolean value is true dict as { index : index whose value is true in pred }
      i = 0
      j = 0
      index = 0      
      final_res = {}
      while j < 17:
          if pred[i, j]:
              final_res[index] = j
              index += 1
          j += 1
      
      data_file.write("\n\nFinal result => " + str(final_res)+'\n')
      
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
                    
      data_file.close()
      return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=predictions[0])
      
if __name__ == '__main__':
   app.run(debug = True)
