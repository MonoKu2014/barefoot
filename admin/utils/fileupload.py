

def handle_uploaded_file(f,nombre):
    with open(nombre, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
