from flask import Flask,render_template,redirect,request
from config import td
import mysql.connector

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    data=request.form
    age=int(data["age"])
    education=int(data["education"])
    default=int(data["default"])
    balance=int(data["balance"])
    housing=int(data["housing"])
    loan=int(data["loan"])
    day=int(data["day"])
    month=int(data["month"])
    duration=int(data["duration"])
    campaign=int(data["campaign"])
    pdays=int(data["pdays"])
    previous=int(data["previous"])
    job=data["job"]
    marital=data["marital"]
    poutcome=data["poutcome"]

    result=td(age,education,default,balance,housing,loan,day,month,duration,campaign,pdays,previous,job,marital,poutcome).output()
    result=int(result[0])

    conn=mysql.connector.connect(host="localhost",database="sac",user="root",password="SachinG!7396")
    cursor=conn.cursor()
    query="insert into td(age,education,def,balance,housing,loan,day,month,duration,campaign,pdays,previous,job,marital,poutcome,output) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    info=(age,education,default,balance,housing,loan,day,month,duration,campaign,pdays,previous,job,marital,poutcome,result)
    cursor.execute(query,info)
    conn.commit()
    conn.close()

    return render_template("index.html",Result=result)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=False)



