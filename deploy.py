from flask import Flask, render_template, request
import pickle




app=Flask(__name__)
#load the model
model=pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result=''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Age=float(request.form['Age'])
    
    tmpSex=request.form['Sex']
    
    if tmpSex=="M":
        tmpSex=1

    
    else:
        tmpSex=0
    
    Sex=float(tmpSex)

    if tmpBP=="HIGH":
        tmpBP=3

    
    elif tmpBP=="NORMAL":
        tmpBP=2
    else:
        tmpBP=1
    BP=float(tmpBP)

    tmpCholesterol=request.form['Cholestrol']

    if tmpCholesterol=="HIGH":
        tmpCholesterol=1

    
    else:
        tmpCholesterol=0
    Cholesterol=float(tmpCholesterol)

    Na_to_K=float(request.form['Na_to_K'])


    
    
    result=model.predict([[Age, Sex, BP, Cholesterol,  Na_to_K]])[0]
    if result == 0:
        return render_template('index.html', Drug='DrugA should be given to patient for better improvement!')
    elif result == 1:
        return render_template('index.html', Drug='DrugB should be given to patient for better improvement!')
    elif result == 2:
        return render_template('index.html', Drug='DrugC should be given to patient for better improvement!')
    elif result == 3:
        return render_template('index.html', Drug='DrugX should be given to patient for better improvement!')
    else:
        return render_template('index.html', Drug='DrugY should be given to patient for better improvement!')



if __name__=="__main__":
    app.run(debug=True)