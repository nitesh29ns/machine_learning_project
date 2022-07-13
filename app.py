from flask import Flask, jsonify
import sys
from housing.logger import lg
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/", methods=('GET','POST'))
def index():
    try :
        raise Exception("we are testing custom exception.")
    except Exception as e:
        housing = HousingException(e,sys)
        lg.info(housing.error_message)
        lg.info("we are testing logger module")
    return "this is my first ml project --> before and after ci/cd pipline this is updated textgit  "

if __name__=="__main__":
    app.run(debug=True)