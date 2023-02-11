from flask import Flask, render_template, request
app = Flask(__name__)
    

@app.route('/')                           
def hello_world():
    return render_template('index.html')  
    
@app.route('/process_form', methods=['POST'])
def process_form(): 
    name = request.form["name"]
    location = request.form["location"]
    fav_language = request.form["fav_language"]
    comment = request.form["comment"]
    return render_template("form_submission.html", name=name, location=location, fav_language=fav_language, comment=comment)







if __name__=="__main__":
    app.run(debug=True)  