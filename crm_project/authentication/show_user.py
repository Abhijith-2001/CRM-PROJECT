# Context Processor
# It is used to implement how a username is displayed.

# It accepts an http response and returns a dictionary.


def show_user_name(request):
    
    username = request.user.username
    
    name = username.split('@')[0]
    
    return { 'User' : name }