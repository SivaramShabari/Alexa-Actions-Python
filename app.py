from flask import Flask, request
from flask_ask import Ask, question, session
from flask_ask.models import statement
from ssml_builder.core import Speech
import pymongo
import json
import google_actions as actions
import alexa_skills as alexa
import api_call_functions as api

app = Flask(__name__)
ask = Ask(app,'/learning_matters')

dbClient = pymongo.MongoClient("mongodb+srv://Narmadha:Secure321@cluster0.s40ur.mongodb.net/learningMatters?retryWrites=true&w=majority")
db=dbClient['learningmatters']

@app.route('/',methods=['GET','POST'])
def func():
    return {"hello":"world. Welcome to home page"}

@app.route('/new',methods=['GET','POST'])
def func():
    return {"hello":"world"}


@ask.on_session_started
def new_session():
    return 'new session started'

@app.before_request
def func():
    session.modified = True

def set_session_attributes(name,value):
    session.attributes[name]=value

def get_session_attributes(name):
    return session.attributes[name]

def get_info():
    return "Dummy data that has to be replaced with Database records"
    
@ask.launch
def start_skill():
    welcome_message = api.introSpeech()
    set_session_attributes('intent','launch')
    return question(welcome_message)

@ask.intent("AMAZON.YesIntent")
def share_info_():
    info = get_info()
    if get_session_attributes('intent')=='teachalphabet':
        info_message = 'Here is the information that you asked for... {}'.format(info)
    elif get_session_attributes('intent')=='selfintro':
        info_message='Great! When you are set say "I am ready to introduce myself...'
    return question(info_message)

@ask.intent("AMAZON.NoIntent")
def no_intent():
    message="Alright...Goodbye"
    return question(message)

@ask.intent("TeachAlphabetsIntent",mapping={'num':'number'})
def start_teaching_alphabets(num):
    teach_message= "Start teaching intent from Flask app...So you know the first {} alphabets! That is great..".format(num)
    set_session_attributes('intent','teachalphabets')
    return question(teach_message)

@ask.intent("IntroductionIntent",mapping={'nam':'name'})
def self_intro(nam):
    speech =Speech()
    speech.add_text("Hello {}! Here is a sample audio of a person introducting herself. Listen to it...".format(nam))
    speech.audio('https://learning-matters-protosem-audio-samples.s3.ap-south-1.amazonaws.com/intro-jencita-1.mp3')
    speech.add_text("Do you want to hear it again? Say yes to proceed...")
    set_session_attributes('intent','selfintro')
    return question(speech.speak())

@ask.intent("StudyIntent",mapping={'type':'TYPE','sub':'SUBJECT',"lesson":"LESSON","lesson_name":"LESSON_NAME"})
def study_intent(type,sub,lesson,lesson_name):
    return question(alexa.studyContent(type,sub,lesson,lesson_name,db))
    

@ask.intent("SayAllLessonsInSubject",mapping={'sub':"SUBJECT_","lesson":"LESSON_"})
def get_contents(sub,lesson):
    speech = Speech()
    col=db["{}".format(sub.lower())]
    if col.count_documents({"type":"{}".format(lesson.lower())},limit = 1)!=0:
        topics = col.find({"type":"{}".format(lesson.lower())})
        topics_list=''
        for x in topics:
            topics_list=topics_list+'{}, '.format(x['name'])
        print(topics_list)
        speech.add_text("The topics available in {} lesson in {} subject are... : ".format(lesson,sub))
        speech.add_text("{}".format(topics_list))
    else:
        speech.add_text("There are no topics in the lesson {} in {} subject".format(lesson,sub))
    return question(speech.speak())

@ask.intent("AMAZON.CancelIntent")
def cancel():
    return statement("Goodbye!")

@ask.intent("AMAZON.StopIntent")
def cancel():
    return statement("Goodbye!")

@ask.intent("AMAZON.FallbackIntent")
def fallback():
    return question("Sorry, I don't understand. Can you please try again?")

@ask.session_ended
def session_ended():
    return"{}", 200
    

#################################
#         GOOGLE ACTIONS:       #
#################################

@app.route('/google', methods=['POST'])
def webhook():
    return actions.action(request)


   
if __name__ == '__main__ ':
    app.run(debug=True)
