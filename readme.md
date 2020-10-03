
## Used commands:
* #### For start the dev project

    
    docker-compose up -d --build
    
* #### For logs information

    
    docker-compose logs -f

* #### For create super user
    
    
    docker-compose exec web python manage.py createsuperuser
    
    


####  Lesson 1 - Basic template of Django Model-View-Template in docker

* docker-compose && Dockerfile structure
* GIT (optional)

* settings:
    * Debug
    * Secret key
    * Installed apps
    * Middleware
    * i18n
* urls:
     * urls_patterns
     * app_name, namespace
     * include
     * StaticRoot, MediaRoot
* views:
    * functions views
    * class based views
    * render
    * CRUD
  
* models:
    * post model
    * ForeignKey
    * get_absolute_url - reverse() function
    * Django Shell Plus
    * 
    
* django-admin
    * rendering
    
    
    

