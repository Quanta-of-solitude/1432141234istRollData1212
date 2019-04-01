import os
from flask import Flask, jsonify, request
import requests
import json
import time

__author__ = "Nyzex"


app = Flask(__name__)


@app.route('/')
def welcome():

    data = "<h1>Welcome!</h1><br><pr>Nothing much to check in here go to /ist/[rollno] for info on the student<br>Eg:/ist/180101001<br>You can use this API for purposes related to Attendence or just info purpose,use it with an app to get images and stuff, think what to do later<br><br><br>PS:I am lazy to design this page :3<br><br><br><br><br><br><br><br><br><br><br><br><br><br>Made By: Nyzex<br><br><br>DataFeed: JordenPiu (Yet to be added)</p>"
    return data

@app.route('/ist/<string:rollno>')
def get_info(rollno):


    try:
        url = "{}".format(os.environ.get("rollLink"))
        dataUnFormatted = requests.get(url)
        dataJson = json.loads(dataUnFormatted.content)
        studentInfo = dataJson['{}'.format(rollno)]
    #    print(dataJson)
        print(studentInfo)
        return jsonify(studentInfo)
    except Exception as e:
        return jsonify({"Error": "Couldn't find the info, SORRY XD"})




if __name__ == '__main__':
    while True:
        app.run()
        time.sleep(40)
