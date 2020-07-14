from django import template

register = template.Library() #registering template filter

def cuted(value,arg):
    """
    This cuts out all the values of 'arg' from the string
    """
    return value.replace(arg,'')


register.filter(name='cuted',cuted)  #first argument is the name you want to give to the filter and second is the call to that function
