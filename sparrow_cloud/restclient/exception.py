# -*- coding: utf-8 -*-

from rest_framework.exceptions import APIException
from rest_framework import status


class HTTPException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ''
    default_code = ''

    def __init__(self, detail=None, code=None):
        try:
            super(HTTPException, self).__init__(detail=detail, code=code)
        except:
            super(HTTPException, self).__init__(detail=detail)