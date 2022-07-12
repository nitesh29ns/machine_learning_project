from flask import Flask, jsonify

app=Flask(__name__)

@app.route("/", methods=('GET','POST'))
def index():
    return "this is my first ml project --> before and after ci/cd pipline this is updated textgit  "

if __name__=="__main__":
    app.run(debug=True)