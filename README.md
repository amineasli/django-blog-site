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
4. Provide initial data for models 
   ```sh
    python manage.py loaddata fixtures/user.json 
    python manage.py loaddata fixtures/tag.json 
    python manage.py loaddata fixtures/post.json 
   ```
5. Run the development server
   ```sh
    python manage.py runserver
   ```
6. You can access the admin via http://127.0.0.1:8000/admin    
   login: admin  
   password: secret
 
## License

Distributed under the MIT License. See `LICENSE` for more information.