
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
    return redirect(url_for('questionmaker'))

@app.route('/')
def questionmaker():
    
    session = DBSession()
    # if var_session.get('used_question')!=None:
    #     if (len(g.used_question) < 1 ) or (len(g.used_question) < 2 ):   
    #         picked = randomizer()
    #     else:
    #         picked = g.used_question[1:]
    # else:
    picked=randomizer()
    if 0 not in picked:
        questions = session.query(Questions).all()  
        choices = session.query(Choices).all()
        
        #     picked = randomizer()
        print(picked)
        session.close()
        return render_template('questiontodelete.html' ,choices = choices,questions=questions,picked=picked)
    else:
        return render_template('full.html')
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
            print(questions.id)
            usedquest = session.query(Used).filter_by(question_id=i).one()
            session.delete(usedquest)
            session.commit()    
        correct = count
        if len(request.form.keys()) > 0:
            count=count*100//len(request.form.keys())  
        else:
            count = 0
        
        session.close()
      

    return render_template('grade.html',grade = count, count =correct)
def randomizer():
    session = DBSession()

    last = session.query(Questions).order_by(Questions.id.desc()).first()
    try:
        if  session.query(Used).one_or_none() != None:
            used=session.query(Used).all()
            for i in used: 
                used_question=used.question_id
        else:
            used_question=[]
    except MultipleResultsFound:
        used=session.query(Used).all()
        print(used)
        used_question=[]
        for i in used: 
            used_question.append(i.question_id)
    tbu=[]
    
    print(used_question)
    if len(used_question) < last.id-3:
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
    print(used_question)
    print(tbu)
    return tbu 





if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=8000)