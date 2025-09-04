"# Pet Adoption API" 
#  Pet Adoption API

A Django REST Framework (DRF) API for managing **users**, **pets**, **adoption requests**, and **reviews**. Supports both **normal users** and **admins** with role-based permissions.

---

##  Setup

1. Clone the repo:

     bash
   git clone https://github.com/Ja11ly/pet_adoption_app.git
   cd pet_adoption_app
   

2. Install dependencies:

      bash
   pip install -r requirements.txt
   

3. Apply migrations:

     bash
   python manage.py migrate
   

4. Create a superuser (admin):

   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

   The API will be available at: `http://127.0.0.1:8000/`



##  Authentication

Authentication is done via **JWT tokens**.

* **Login:**

  ```http
  POST http://127.0.0.1:8000/api/auth/token/
  {
    "username": "name",
    "password": "*****"
  }
  ```

  Returns access + refresh tokens.



##  Users

### Create User

```http
POST http://127.0.0.1:8000/api/users/
{
  "username": "name",
  "email": "example@test.com",
  "password": "*****"
}
```

* Accessible by: **Anyone (registration)**

### Get Users

```http
GET http://127.0.0.1:8000/api/users/
```

* Accessible by: **Admin only**

### Get Single User

```http
GET http://127.0.0.1:8000/api/users/<id>/
```

* Accessible by: **Admin only**
* Supports filtering.

### Update User

```http
PATCH http://127.0.0.1:8000/api/users/<id>/
```

* Accessible by: **Admin & the user themselves**

### Delete User

```http
DELETE http://127.0.0.1:8000/api/users/<id>/
```

* Accessible by: **Admin only**



##  Pets

### Get Pets

```http
GET http://127.0.0.1:8000/api/pets/
```

* Accessible by: **Admin & Normal Users**
* Supports filtering (by breed, location, species).

### Create Pet

```http
POST http://127.0.0.1:8000/api/pets/
{
  "name": "Buddy",
  "breed": "Terrier",
  "age": "2",
  "location": "Nairobi",
  "species": "Dog"
}
```

* Accessible by: **Admin only**

### Update Pet

```http
PATCH http://127.0.0.1:8000/api/pets/<id>/
```

* Accessible by: **Admin only**

### Delete Pet

```http
DELETE http://127.0.0.1:8000/api/pets/<id>/
```

* Accessible by: **Admin only**



##  Adoption Requests

### Create Adoption Request

```http
POST http://127.0.0.1:8000/api/adoptions/
{
  "pet": 4,
  "user": 2,
  "status": "pending",
  "message": "I would like to adopt this pet."
}
```

* Accessible by: **Normal Users & Admins**

### Get Adoption Requests

```http
GET http://127.0.0.1:8000/api/adoptions/
```

* Accessible by: **Admin only**
* Supports filtering (by user, pet, status).

### Update Adoption Request

```http
PATCH http://127.0.0.1:8000/api/adoptions/<id>/
```

* Accessible by: **Admin only** (update status: approved/rejected/pending)

### Delete Adoption Request

```http
DELETE http://127.0.0.1:8000/api/adoptions/<id>/
```

* Accessible by: **Admin only**



## ⭐ Reviews

### Create Review

```http
POST http://127.0.0.1:8000/api/reviews/
{
  "pet": 4,
  "rating": 5,
  "comment": "Lovely dog, very friendly!"
}
```

* Accessible by: **Normal Users & Admins**

### Get Reviews

```http
GET http://127.0.0.1:8000/api/reviews/
```

* Accessible by: **All authenticated users**
* Supports filtering (by pet, user, rating).

### Update Review

```http
PATCH http://127.0.0.1:8000/api/reviews/<id>/
```

* Accessible by: **Author (normal user) & Admin**

### Delete Review

```http
DELETE http://127.0.0.1:8000/api/reviews/<id>/
```

* Accessible by: **Author & Admin**

---

##  Filtering

Available on **Users, Pets, Adoptions, Reviews**.

Examples:

```http
GET http://127.0.0.1:8000/api/pets/?species=dog
GET http://127.0.0.1:8000/api/pets/?location=Nairobi
GET http://127.0.0.1:8000/api/reviews/?rating=5
GET http://127.0.0.1:8000/api/adoptions/?status=pending
```

---

##  Role Breakdown

###  Normal User

* Register & login
* View pets
* Request pet adoptions
* Post, edit, and delete **their own** reviews
* Edit **their own** profile

###  Admin (via superuser)

* Full access to **all users**
* Manage **all pets** (CRUD)
* Approve/reject/delete adoption requests
* Manage **all reviews**