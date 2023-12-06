from django.urls import path
from .views import IndexView, QuestionDetailView, ResultsView, VoteView

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='detail'),
    path('vote/<int:question_id>/', VoteView.as_view(), name='vote'),
    path('results/<int:pk>/', ResultsView.as_view(), name='results'),
]
