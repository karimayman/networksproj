
from flask import Flask, render_template, request, redirect, url_for, \
    jsonify
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Questions, Choices
from flask import session as var_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
app = Flask(__name__)

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
#session = DBSession()
@app.route('/')
def questionmaker():
    
    session = DBSession()
    # if var_session.get('used_question')!=None:
    #     if (len(var_session['used_question']) < 1 ) or (len(var_session['used_question']) < 2 ):   
    #         picked = randomizer()
    #     else:
    #         picked = var_session['used_question'][1:]
    # else:
    #     picked = randomizer()
    picked=randomizer()
    questions = session.query(Questions).all()  
    choices = session.query(Choices).all()
    session.close()
    var_session.modified=True
    return render_template('questiontodelete.html' ,choices = choices,questions=questions,picked=picked)
@app.route('/graded', methods=['POST'])
def grader():
    grade = 0
    if request.method == 'POST':
        count = 0
        session = DBSession()
        for i in request.form.keys():
            questions = session.query(Questions).filter_by(id=i).one()   
            if request.form[i] == questions.answer:
                count+=1   
            print(var_session['used_question'])
            print(questions.id)
            var_session['used_question'].remove(questions.id)    
        correct = count
        if len(request.form.keys()) > 0:
            count=count*100//len(request.form.keys())  
        else:
            count = 0
        print(var_session['used_question'])
        session.close()
        #del var_session['used_question']
        #var_session.clear()
        var_session.modified=True

    return render_template('grade.html',grade = count, count =correct)
def randomizer():
    session = DBSession()

    last = session.query(Questions).order_by(Questions.id.desc()).first()
    rangelist=range(1,last.id+1)
    tbu=[]

    if var_session.get('used_question')==None:
        var_session['used_question']=[0]
    print(var_session['used_question'])
    for i in range(3):
        not_used=random.choice([x for x in range(1,last.id+1) if x not in var_session['used_question']])
        var_session['used_question'].append(not_used)
        tbu.append(not_used)
    session.close()
    print(var_session['used_question'])
    print(tbu)
    return tbu





if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=8000)