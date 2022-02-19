from flask import Flask,jsonify,request

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "HELLO USER"
task=[{"Id":1,"Name":"Shivanshu","Contact":"4862513954","done":False},
{"Id":2,"Name":"Gautam","Contact":"1716852344","done":False}]

@app.route("/Add_Data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({"status":"ERROR","message":"PLEASE PROVIDE DATA"},400)
    tasks={
        "Id":task[-1]["Id"]+1,"Name":request.json["Name"],"Contact":request.json.get("Contact",""),"done":False
    }
    task.append(tasks)
    return jsonify({"status":"SUCCESS","message":"CONTACT ADDED SUCCESsFULLY"})

@app.route("/Get_data")
def get_task():
    return jsonify({"data":task})

if (__name__ == "__main__"):
    app.run(debug=True)