import api_calls as api
import google_actions_functions as action
def action(request):
    handler_type = request.json["handler"]["name"]

    print("\nFrom module...")
    print(request.data)
    print("\nHandler:")
    print(handler_type)

    if(handler_type=='greeting'):
        speech = api.introSpeech()
        return action.prompt(request, speech)

    elif(handler_type=='teachContentScene'):
        speech = api.teachContentSpeech()
        return action.prompt(request, speech)

    elif(handler_type=='slotValidation'):
        return action.slotHandler(request)
    
    elif(handler_type=='teachContentFilled'):
        slots = request.json['scene']['slots']
        content = api.getTopicContent(slots['subject']['value'],slots['lesson']['value'])
        return action.prompt(request, content)

    elif(handler_type=='repeatTeaching'):
        slots = request.json['scene']['slots']
        content = api.getTopicContentRepeat(slots['subject']['value'],slots['lesson']['value'])
        return action.prompt(request, content)

    else:
        return action.speakAndEndConversation(request,"Oopsies! There was a error processing your request! We will fix that soon")
    

