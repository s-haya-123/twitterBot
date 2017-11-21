from rest_framework import routers
from .views import HistoryViewSet, NagoyanSakuraSet, HistoryFilterViewSet
from django.conf.urls import url,include
from . import views


router = routers.DefaultRouter()
router.register(r'nagoyan', NagoyanSakuraSet)

urlpatterns = [
    url(r'^$', include(router.urls)),
    url(r'^v1/(?P<title>[\w]+)/$', HistoryFilterViewSet.as_view()),
]