from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import status
from rest_framework             import viewsets
from rest_framework.authentication import TokenAuthentication


from profiles_api               import serializers
from profiles_api               import models
from profiles_api               import permissions

class HelloAPIView(APIView):
    """ API view class   """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of API view features  """
        an_apiview = ['Uses HTTP methods as fucntion (get, post, put, patch, delete)',
            'Is simliar to traditional Djanog view',
            ' Mapped to URLs'
            ]

        return Response({'message': 'Hello', 'an_apiview':an_apiview })

    def post(self, request, ):
        """ Creates a hello message with our name  """
        serializer = self.serializer_class(data =  request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
             )

    def put(self, request, pk=None):
        """ Hanlde updating an object  """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle partial update of  an object  """

        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """ Delete   an object  """

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test APIViewset """
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """ Retutn Hello message """

        a_viewset = ['Uses actions (list, create, retrieve, update, partial_update, delete)',
            'Automatically maps to URLs using Routers',
            ' Provides more functionality with less code'
            ]

        return Response({'message': 'Hello', 'a_viewset':a_viewset })


    def create(self, request):
        """ Retutn Hello message """

        serializer = self.serializer_class(data =  request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
             )

    def retrieve(self, reques,pk=None):
        """ Hanlde getting  an object by its id """

        return Response({'http method': 'GET'})

    def update(self, reques, pk=None):
        """ Hanlde updating   an object by its id """

        return Response({'http method': 'PUT'})


    def partial_update(self, reques, pk=None):
        """ Hanlde partila updating   an object by its id """

        return Response({'http method': 'PATCH'})


    def destroy(self, reques, pk=None):
        """ Hanlde removing   an object by its id """

        return Response({'http method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
