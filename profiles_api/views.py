from django.shortcuts           import render
from rest_framework.views       import APIView
from rest_framework.response    import Response

class HelloAPIView(APIView):
    """ API view class   """

    def get(self, request, format=None):
        """ Returns a list of API view features  """
        an_apiview = ['Uses HTTP methods as fucntion (get, post, put, patch, delete)',
            'Is simliar to traditional Djanog view',
            ' Mapped to URLs'
            ]

        return Response({'message': 'Hello', 'an_apiview':an_apiview })
