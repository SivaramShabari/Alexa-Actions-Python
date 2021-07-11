from ssml_builder.core import Speech

def studyContent(type,sub,lesson,lesson_name,db):
    speech = Speech()
    if(type=="learn" or type =="Learn" or type=="study"):
        col=db["{}".format(sub.lower())]
        if col.count_documents({"type":"{}".format(lesson.lower())},limit = 1)!=0:           
            query=col.find_one({'name':"{}".format(lesson_name)})
            speech.add_text("You have chosen to {} {} from {}. That is great! Lets get started...".format(type,lesson_name,sub))
            speech.audio('https://learning-matters-protosem-audio-samples.s3.ap-south-1.amazonaws.com/baba-black-sheep.mp3')
            #speech.add_text(query['content'])
               
        else:
            speech.add_text("Sorry. The given lesson name does not exist!")
    else:
        col=db["{}".format(sub.lower())]
        if col.find({'name':lesson_name}).count>0:
            query=col.find_one({'name':lesson_name})
            speech.add_text("You have chosen to {} {} from {}. That is great! Lets get started...".format(type,lesson_name,sub))
            speech.add_text(query[0]['type'])
        else:
            speech.add_text("Sorry. The given lesson name does not exist!")
    return speech.speak()