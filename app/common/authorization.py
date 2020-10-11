from survey.models import Token
import jwt

class Authorization(object):

    @classmethod
    def authorize_token(cls,encoded_token):
        try:
            decoded_token = jwt.decode(encoded_token, 'secret', algorithms=['HS256'])
        except:
            return False
        token = decoded_token['token']

        try:
            token_obj = Token.objects.get(session_token=token)
            return True
        except Token.DoesNotExist:
            return False