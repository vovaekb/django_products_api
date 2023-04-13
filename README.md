# django_products_api


🛍️ Simple REST API application on Python Django REST Framework.

Features:
- admin panel with ability to edit products and categories
- list products and categories in JSON format
- using Swagger documentation

## Run application
Clone the repo, change to the project root folder. Install dependencies from requirements.txt file:

```bash
pip install -r requirements.txt
```
Run the application:
```bash
python manage.py runserver
```

Open admin panel: http://127.0.0.1:8000/admin. Under admin account you can edit lessons and teachers in database. 
To see products API data open page:  http://127.0.0.1:8000/api/products/.

To see categories API data open page:  http://127.0.0.1:8000/api/categories/.

To see Swagger documentation open page: http://127.0.0.1:8000/swagger/.
