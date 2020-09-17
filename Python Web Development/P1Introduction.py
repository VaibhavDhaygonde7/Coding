import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template('index.html')  #this will include index.html in this python file 
    #this function will be executed if the end of the address is /

@app.route("/vaibhav")
def vaibhav():
    #passing variable to a function 
    name = "Vaibhav"
    return flask.render_template('about.html', name2=name)  #this variable will be used in the about.html
    #we have written here 'name' which is written in the about.html in the h1 tag
    #this function will be executed if the end of the address is /vaibhav

app.run(debug=True)    #this will run the app 
#debug=True will allow us to reload the page and get the fresh output