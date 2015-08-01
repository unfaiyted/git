from django.http import HttpResponse

from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter

from .config import CONFIG
# Create your views here.

authomatic = Authomatic(CONFIG, 'a super secret randomz string')


def home(request):
    return HttpResponse('''
        Login with <a href="login/fb">Facebook</a>.</br>
        <form action="login/oi">
            <input type="text" name="id" value="me.yahoo.com" />
            <input type="submit" value="Auth with OpenID" />
        </form>
        ''')


def login(request, provider_name):
    # We need the response object for the adapter
    response = HttpResponse()

    # Start the login procedure
    result = authomatic.login(DjangoAdapter(request, response), provider_name)

    # If there is no result, the login procedure is still pending.
    # Don't write anything to the response if there is no result.
    if result:
        # if there is result, the login procedure is over and we can write to response.
        response.write('<a href="..">Home</a>')

        if result.error:
            # Login there is result, the login procedures is over and we can write to response.
            response.write(u'<h2>Damn that error: {0}</h2>'.format(request.GET.get("error_message")))

        elif result.user:
            # Hooray, it actually worked and we have a user

            # If we can get into the users information
            if not (result.user.name and result.user.id):
                result.user.update()
                response.write(u'<h1>Hi {0}</h1>'.format(result.user.name))
                response.write(u'<h2>Your id is: {0}</h2>'.format(result.user.id))
                response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))
                if result.user.credentials:

                    # Facebook API:
                    if result.provider.name == 'fb':
                        response.write('You are logged in with Facebook.<br />')

                    else:
                        response.write('Damn that unknownn error!<br />')
                        response.write(u'Status: {0}'.format(response.status))

    return response
