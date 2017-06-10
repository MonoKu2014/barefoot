from django.shortcuts import redirect


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        path=request.path

        if path!='/' and path!='/reset_password' and path!='/check_code':
            if request.session.get('user')is None:
               return redirect('/')

        if path =='/reset_password' or path=='/check_code' :
            if request.method != 'POST':
               return redirect('/')
        response = self.get_response(request)
        return response