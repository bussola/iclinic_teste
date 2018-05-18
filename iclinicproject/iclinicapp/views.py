from iclinicapp.models import Agenda
from iclinicapp.serializers import AgendaSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from iclinicapp.serializers import UserSerializer
from rest_framework import permissions
from iclinicapp.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.decorators import action


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'agendamento': reverse('agenda-list', request=request, format=format)
    })


class AgendaViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     agenda = self.get_object()
    #     return Response(agenda.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer