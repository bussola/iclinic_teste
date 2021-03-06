from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from iclinicapp import views
#from rest_framework.schemas import get_schema_view


from rest_framework_swagger.views import get_swagger_view



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'agendamento', views.AgendaViewSet)
router.register(r'users', views.UserViewSet)

#schema_view = get_schema_view(title='Pastebin API')
schema_view = get_swagger_view(title='Agendamento API')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/$', schema_view),
]