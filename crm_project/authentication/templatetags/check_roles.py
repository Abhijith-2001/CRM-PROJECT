from django import template


register = template.Library()


# @register.simple_tag
# def lowercase(word):
    
#     return word.lower()


# @register.simple_tag

# def check_user_role(request,roles):

#     roles = roles.split(',')

#     allow = False

#     if request.user.role in roles:

#         allow = True
    
#     return allow






@register.simple_tag
def check_user_role(request, roles):
   
    if not request or not hasattr(request, 'user'):
        
        return False                                    # Ensure request and user exist

    user_role = getattr(request.user, 'role', None)     # Get user's role safely
    
    if not user_role:
        
        return False                                    # Return False if the user has no role

    allowed_roles = roles.split(',')                    # Convert roles string to a list
    
    return user_role in allowed_roles                   # Return True if user's role is allowed