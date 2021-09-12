from flask import Flask,jsonify

app = Flask (__name__)
courses=[{"name":"python programming",
          "course_id":"0",
          },
         {"name":"python programming advance",
          "course_id":"1"}]
@app.route('/')
def index():
    return "Welcome To The Course API"



@app.route("/courses",methods=["GET"])
def get():
    return jsonify({"courses":courses})
@app.route("/courses/<int:course_id>",methods=["GET"])
def get_course(course_id):
    return jsonify({'course':course_id})
if __name__=="__main__":
    app.run(debug=True)
