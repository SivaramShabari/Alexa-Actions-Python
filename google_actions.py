import api_call_functions as api
def action(request):
    handler_type = request.json["handler"]["name"]

    print("From module :")
    print(request.data)

    if(handler_type=='greeting'):
        speech = api.introSpeech()
        return prompt(request, speech)

    # elif(handler_type=='teachContentScene'):
    #     speech = api.teachContentSpeech()
    #     return prompt(request, speech)

    # elif(handler_type=='getSubjectSlot'):
    #     return setSlotTeachContent(request,"Okay! Let us learn someyhing today Hmm.. Which subject do you want to learn?",'subject')
    
    # elif(handler_type=='getLessonSlot'):
    #     slots = request.json['scene']['slots']
    #     return setSlotTeachContent(request,"In {}, which lesson do you want to learn?".format(slots['subject']['value']),'lesson')

    # elif(handler_type=='getTopicSlot'):
    #     slots = request.json['scene']['slots']
    #     return setSlotTeachContent(request,"Great. In {}, which topic do you want to learn?".format(slots['lesson']['value']),'lesson')

    elif(handler_type=='teachContentFilled'):
        slots = request.json['scene']['slots']
        return prompt(request,api.getTopicContent(slots['subject']['value'],slots['lesson']['value'],slots['topic']['value'])+""". Say please repeat to repeat the topic. 
        If you have learnt the topic, then well done!, say cancel to end this lesson.""")

    elif(handler_type=='repeatContent'):
        slots = request.json['scene']['slots']
        return prompt(request,api.getTopicContent(slots['subject']['value'],slots['lesson']['value'],slots['topic']['value'])+""". Say please repeat to repeat the topic. 
        If you have learnt the topic, then well done!, say cancel to end this lesson.""")

    else:
        return speakAndEndConversation(request,"Oopsies! There was a error processing your request! We will fix that soon")
    


def prompt(request,speech):
    return {
        "session": {
            "id":request.json["session"]["id"] ,
            "params": request.json["session"]["params"]
        },
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": speech,
                "text": speech
           }
        },
        "scene": {
            "name": request.json["scene"]["name"],
            "slots":request.json["scene"]["slots"]
        }
    }



def setSlotTeachContent():
    return {
        "scene": {
            "name": "TeachContent",
            "slotFillingStatus": "FINAL",
            "slots": {
                "lesson": {
                    "mode": "REQUIRED",
                    "status": "SLOT_UNSPECIFIED",
                    "updated": false,
                    "value": "poems"
                },
                "subject": {
                    "mode": "REQUIRED",
                    "status": "SLOT_UNSPECIFIED",
                    "updated": false,
                    "value": "english"
                },
                "topic": {
                    "mode": "REQUIRED",
                    "status": "SLOT_UNSPECIFIED",
                    "updated": true,
                    "value": "coin"
                }
            }
        }
    }

def speakAndEndConversation(request,speech):
    return {
        "session": {
            "id":request.json["session"]["id"] ,
            "params": request.json["session"]["params"]
        },
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": speech,
                "text": speech
            }
        },
        "scene": {
            "name": request.json["scene"]["name"],
            "slots":request.json["scene"]["slots"] ,
            "next": {
                "name": "actions.scene.END_CONVERSATION"
            }
        }
    }


