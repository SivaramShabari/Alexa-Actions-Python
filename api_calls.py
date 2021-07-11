import pyrebase 

firebaseConfig = {
    "apiKey": "AIzaSyA2YsnCNc9cAFOsIL7qNweRF7gMzRugCWo",
    "authDomain": "learningmattersprotosem.firebaseapp.com",
    "databaseURL": "https://learningmattersprotosem-default-rtdb.firebaseio.com",
    "projectId": "learningmattersprotosem",
    "storageBucket": "learningmattersprotosem.appspot.com",
    "messagingSenderId": "585768616134",
    "appId": "1:585768616134:web:4b345a33b968ad225dd7c7"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").child("Morty").set(data)

def getLessonsBySubject():
    return "lessons"

def getAllSubjects():
    return "Subjetcs"

def introSpeech():
    return 'Welcome to learning matters. I can teach you many things!! Say teach me something to get started...'

def getTestContent():
    return "test content"

def teachContentSpeech():
    return "Ok, let us learn something today!!"

def getTopicContent(subject,lesson):
    speech = "Awesome! You've chosen to learn lesson {} from {} subject! Let's get started! ".format(lesson,subject)
    content = "Users are limited to a rolling window of 75 requests to Heroku Git repos per hour, per app, per user. The uncompressed size of a checkout of HEAD from the repo, combined with the size of restored submodules, cannot exceed 1 GB. "
    extra = "If you wan't me to repeat the content, please say \"repeat it again\". If you have learnt the lesson then great!, say quit to exit. "
    return speech+content+extra

def getTopicContent(subject,lesson):
    speech = "Ok! I will repeat it again... ".format(lesson,subject)
    content = "\nUsers are limited to a rolling window of 75 requests to Heroku Git repos per hour, per app, per user. The uncompressed size of a checkout of HEAD from the repo, combined with the size of restored submodules, cannot exceed 1 GB. "
    extra = "If you wan't me to repeat the content, please say \"repeat it again\". If you have learnt the lesson then great!, say quit to exit. "
    return speech+content+extra