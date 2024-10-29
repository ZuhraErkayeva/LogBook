from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.IndexListView.as_view(), name = 'index'),
    path('about/',views.AboutList.as_view(), name='about'),
    path('book/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_list/',views.PostListView.as_view(), name='post_list'),
    path('privacy/',views.PrivacyListView.as_view(), name='privacy_policy'),
    path('terms/',views.Terms_conditionsListView.as_view(), name='terms_conditions'),
    path('contact/', views.EmailSendView.as_view(), name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)