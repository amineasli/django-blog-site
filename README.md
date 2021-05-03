# Django Blog Site

A simple blog application based on Django

## Installation

1. Clone the repo
   ```sh
    git clone https://github.com/AmineAsli/django-blog-site.git
   ```
2. Install Python packages
   ```sh
    cd django-blog-site/
    pip install -r requirements.txt
   ```
3. Apply migrations
   ```sh
    python manage.py migrate
   ```
4. Collects all the static files into STATIC_ROOT
   ```sh
    python manage.py collectstatic
   ```
5. Provide initial data for models 
   ```sh
    python manage.py loaddata fixtures/user.json 
    python manage.py loaddata fixtures/tag.json 
    python manage.py loaddata fixtures/post.json 
   ```
6. Run the development server
   ```sh
    python manage.py runserver
   ```
7. You can access the admin via http://127.0.0.1:8000/admin    
   login: admin  
   password: secret
  
## Running tests
```sh
 python manage.py test
```
## License

Distributed under the MIT License. See `LICENSE` for more information.
