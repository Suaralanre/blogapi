## Blog API


### Project Description
 This project is a REST API created with Django Rest Framework that aims to display some of the rich features of it as well as Django web framework.
 ### Features 
1. Use of Class Based and Generic Class Based Views all through the project.
2. User authentication
    > It is implemented via the in-built **api-auth**, and 3rd party libraries - **dj-rest-auth(4.0.1)** and **django-allauth(0.54.0)**.
    It also incorporates email authentication when the user registers.
3. Each Custom User is able to:
:star2:	Create their own blog post and see other people's blog post
:star2:	Each Custom User is able to view all of the blog posts.
:star2:  View their own posts ONLY.

5. The views and routes are implemented via viewsets and routers
> This is in contrast to the traditional repetition of multiple related views.

### Installation
You can create a local copy of this project by following these steps:
:point_right:	Preferably create and activate a python virtual environment on your local machine.
:point_right:	Make sure git is installed and setup on your local machine.
:point_right:	From the directory that has the virtual environment, run the following:
> `mkdir blogapi && git clone git@github.com:Suaralanre/blogapi.git`
> `pip install -r requirements.txt`

### Concluson
*Please feel  free to create an issue for suggestions and constructive criticisms*.

Cheers!
