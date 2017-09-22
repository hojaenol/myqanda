from base64 import b64decode, b64encode
from django.utils.six.moves.urllib import parse as urlparse
from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class QandaCursorPagination(CursorPagination):

    # def __init__(self, page_size, ordering):
    #     self.page_size = page_size
    #     self.ordering = ordering
    ordering = '-created_at'

    def get_paginated_response(self, data):
        response = Response(data)
        response['cursor-prev'] = self.get_previous_link()
        response['cursor-next'] = self.get_next_link()
        return response

    def encode_cursor(self, cursor):
        """
        Given a Cursor instance, return an url with encoded cursor.
        """
        tokens = {}
        if cursor.offset != 0:
            tokens['o'] = str(cursor.offset)
        if cursor.reverse:
            tokens['r'] = '1'
        if cursor.position is not None:
            tokens['p'] = cursor.position

        querystring = urlparse.urlencode(tokens, doseq=True)
        encoded = b64encode(querystring.encode('ascii')).decode('ascii')
        return encoded
