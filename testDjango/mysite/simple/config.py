# config.py

from authomatic.providers import oauth2

CONFIG = {

    'fb': {

        'class_': oauth2.Facebook,

        # Facebook is an AuthorizationProvider too.
        'consumer_key': '880482795377664',
        'consumer_secret': 'c1667d953918776901346f70dccf67ce',

        # Is also an OAuth 2.0 Provider and needs scope.for6
        'scope': oauth2.Facebook.user_info_scope + ['publish_actions'],

    },

    'google': {

        'class_': oauth2.Google,
        'consumer_key': 'XXXXXXX',
        'consumer_secret': 'XXXXXXXX',

        'scope': oauth2.Google.user_info_scope + [
            'https://www.googleapis.com/auth/calendar']


    }


}