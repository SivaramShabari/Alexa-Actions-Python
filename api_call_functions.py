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

def getTopicContent(subject,lesson,lesson_name):
    return "Awesome! You've chosen to learn {} from lesson{} from {} subject! Let's get started".format(lesson_name,lesson,subject)