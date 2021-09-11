restaurant_homepage
=====

restaurant_homepage is a modern homepage template for restaurants. The Django app comes in a modern style via Bootstrap 4.

![test](https://github.com/stfab/restaurant_homepage/blob/main/preview/screenshot.png)

Requirements
-----------
restaurant_homepage was developed using Django 2.2 and django-widget-tweaks 1.4.5. 
The Python Version used is 3.7.

* `pip install django`
* `pip install django-widget-tweaks`

Quick start
-----------

0. Copy restaurant_homepage into your django project.

1. Add "restaurant_homepage" and "django-widget-tweaks" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'restaurant_homepage.apps.RestaurantHomepageConfig',
		'widget_tweaks'
    ]

2. Include the forum URLconf in your project urls.py like this:

    path('restaurant_homepage/', include('restaurant_homepage.urls')),

3. Run `python manage.py migrate` to create the forum models.

4. Set your static and media path in your projects settings.py like this:
```
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
5. Add your media path to your urls.py (any pictures will be saved into the media path):

	urlpatterns = [...] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to see the available models (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/restaurant_homepage/ to view the index page.

Notice: Ristorante Roma is a fictional party added for testing purposes.
