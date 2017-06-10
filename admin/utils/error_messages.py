__author__ = 'victorfx'

def required():
    return 'Requerido'

def min_length_message(min,max):

    return 'El Campo debe tener una longitud minima de '+`min`+' y maxima de '+`max`

def min_message(min):
    return 'el campo tiene que tener un valor de minimo '+`min`

def max_message(max):
    return 'el campo tiene que tener un valor de maximo '+`max`

def range_message(min,max):
    return  'el campo debe ser un velor entre '+`min`+' y '+`max`

def email_message():
    return 'Ingrese un Email Valido'

