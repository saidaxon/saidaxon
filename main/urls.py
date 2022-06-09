from django.urls import path
from .views import *
urlpatterns = [
    path ('kitob/',KitobPageView.as_view(), name='kitob'),
    path ('surat/',SuratPageView.as_view(), name='surat'),
    path ('mukofot/',MukofotPageView.as_view(), name='mukofot'),
    path('',index,name='index'),
    path('sherlar/',SherList.as_view(),name='sherlar'),
    path('sher/<int:pk>/', SherDetail.as_view(), name='sher'),
    path('hikoyalar/',HikoyaList.as_view(),name='hikoyalar'),
    path('hikoya/<int:pk>/', HikoyaDetail.as_view(), name='hikoya'),
    path('lavhalar/',LavhaList.as_view(),name='lavhalar'),
    path('lavha/<int:pk>/', LavhaDetail.as_view(), name='lavha'),
    path('etyudlar/',EtyudList.as_view(),name='etyudlar'),
    path('etyud/<int:pk>/', EtyudDetail.as_view(), name='etyud'),
    path('maqolalar/',MaqolaList.as_view(),name='maqolalar'),
    path('maqola/<int:pk>/', MaqolaDetail.as_view(), name='maqola'),
    path('epiklar/',EpikList.as_view(),name='epiklar'),
    path('epik/<int:pk>/', EpikDetail.as_view(), name='epik'),
    path('liriklar/',LirikList.as_view(),name='liriklar'),
    path('lirik/<int:pk>/', LirikDetail.as_view(), name='lirik'),
    path('dramatiklar/',DramaList.as_view(),name='dramatiklar'),
    path('dramatik/<int:pk>/', DramaDetail.as_view(), name='dramatik'),
    path('search/',s,name='search'),


]