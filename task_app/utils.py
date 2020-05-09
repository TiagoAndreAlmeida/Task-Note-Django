from rest_framework.exceptions import APIException

## put your help function here ##

class EmailUnavailable(APIException):
    status_code = 406
    default_detail = 'Já existe um usuário com esse e-mail'
    default_code = 'not_acceptable'