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


def slotHandler(request):
    slots=request.json["scene"]["slots"]
    if slots["lesson"]["updated"]:
        msg = "Ok..."
    else:
        msg = "Ok in {},".format(slots["subject"]["value"])
    response = prompt(request, msg)
    if request.json["scene"]["slotFillingStatus"]=="FINAL" or slots["lesson"]["updated"]:
        response["session"]["params"]["subject"]=request.json["scene"]["slots"]["subject"]["value"]
        response["session"]["params"]["lesson "]=request.json["scene"]["slots"]["lesson "]["value"]
    return response

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
