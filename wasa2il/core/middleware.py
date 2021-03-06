
from django.conf import settings

from core.models import UserProfile


class UserSettingsMiddleware(object):
    def __init__(self):
        pass

    def process_request(self, request):
        if request.user.is_authenticated():
            try:
                request.session['django_language'] = request.user.get_profile().language
            except AttributeError:
                # pass
                pro = UserProfile()
                pro.user = request.user
                pro.language = settings.LANGUAGE_CODE
                pro.save()
                request.session['django_language'] = pro.language
        else:
            request.session['django_language'] = "is"

        print request.LANGUAGE_CODE
