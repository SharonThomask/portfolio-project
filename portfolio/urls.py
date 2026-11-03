
from django.contrib import admin
from django.urls import path
from api.views import AboutView,EducationView,ProjectView,SkillsView,ExperienceView,CertificationView,ServiceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',AboutView.as_view()),
    path('education/',EducationView.as_view()),
    path('projects/',ProjectView.as_view()),
    path('skills/',SkillsView.as_view()),
    path('experiences/',ExperienceView.as_view()),
    path('certification/',CertificationView.as_view()),
    path('service/',ServiceView.as_view())
]
