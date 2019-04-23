
from flask import Flask, render_template,g, request, redirect, url_for, \
    jsonify
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Questions, Choices, Used
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
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

@app.route('/nothere')
def notsafe():

    session = DBSession()
    used = session.query(Used).all()
    for i in used:
        session.delete(i)
        session.commit() 
    session.close()
    used = session.query(Used).all()
    print(used)
    var_session.clear()
    return redirect(url_for('questionmaker'))

@app.route('/')
def questionmaker():
    if var_session.get('used_question')==None:
        picked=randomizer()

        var_session['used_question']=picked
    else:
        picked = var_session['used_question']    
    print(picked)
    session = DBSession()
    # if var_session.get('used_question')!=None:
    #     if (len(g.used_question) < 1 ) or (len(g.used_question) < 2 ):   
    #         picked = randomizer()
    #     else:
    #         picked = g.used_question[1:]
    # else:

    questions = session.query(Questions).all()  
    choices = session.query(Choices).all()
    session.close()        
    if 0 not in picked:

        return render_template('questiontodelete.html' ,choices = choices,questions=questions,picked=picked)
    else:
        return render_template('full.html')
   
@app.route('/graded', methods=['POST'])
def grader():
    print("hello hello")
    grade = 0
    if request.method == 'POST':
        count = 0
        session = DBSession()
        for i in request.form.keys():
            questions = session.query(Questions).filter_by(id=i).one()   
            if request.form[i] == questions.answer:
                count+=1   
            usedquest = session.query(Used).filter_by(question_id=i).one()
            session.delete(usedquest)
            session.commit()    
        correct = count
        if len(request.form.keys()) > 0:
            count=count*100//len(request.form.keys())  
        else:
            count = 0
        
        session.close()
      
        del var_session['used_question']
        var_session.clear()

    return render_template('grade.html',grade = count, count =correct)
def randomizer():
    session = DBSession()

    last = session.query(Questions).order_by(Questions.id.desc()).first()
    try:
        if  session.query(Used).one_or_none() != None:
            used=session.query(Used).all()
            used_question=[]
            for i in used: 
                used_question.append(i.question_id)
        else:
            used_question=[]
    except MultipleResultsFound:
        used=session.query(Used).all()
        used_question=[]
        for i in used: 
            used_question.append(i.question_id)
    tbu=[]
    print(len(used_question))
    if len(used_question) < last.id-1:
        for i in range(3):
            not_used=random.choice([x for x in range(1,last.id+1) if x not in used_question])
            newrec = Used(question_id=not_used)
            session.add(newrec)
            session.commit()
            used_question.append(not_used)
            tbu.append(not_used)
        session.close()
    else:
        tbu=[0]
    return tbu 

# @app.route('/unfinished', methods=['POST'])
# def unfinished():
#     session = DBSession()
#     for i in var_session['used_question']:  
#         print(var_session['used_question'])
#         usedquest = session.query(Used).filter_by(question_id=i).one()
#         session.delete(usedquest)
#         session.commit()    
#     var_session.clear()
#     session.close()
#     print("hello hello hello i worked and everything is cool")
#     return




if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=8000)