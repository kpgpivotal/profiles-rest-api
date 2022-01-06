from rest_framework     import serializers


class HelloSerializer (serializers.Serializer):
    """ Serializes a text field for testing and APIView   """

    name = serializers.CharField(max_length=15)
