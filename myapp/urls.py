from django.urls import path, include
from myapp import views
urlpatterns = [

    path("", views.index, name="home"),
    path("indexPage/", views.indexPage, name="indexPage"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("saveenquiry/", views.saveEnquiry, name="saveenquiry"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio/", views.portfolio_details, name="portfolio"),
    path("services/", views.service, name="services"),
    path("team/", views.team, name="team"),
    path("blogsingle/", views.blogsingle, name="blogsingle"),
    path("Hacking News/", views.Hacking, name="Hacking News")

]
