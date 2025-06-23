# 🎙️ Late Show API

A Flask RESTful API that manages guests, episodes, and appearances on a fictional talk show. It includes user registration and login using JWT authentication, full CRUD support, and a sample Postman collection for testing.

---

## 📦 Project Setup Guide (One Continuous Step)

1. **Clone the Repository and Install Dependencies**

   
   git clone https://github.com/your-username/late-show-api.git
   cd late-show-api
   pipenv install
   pipenv shell
   

2. **Set Up the Environment Variables**

   Create a `.env` file in the root directory with the following contents:

   
   DATABASE_URI=postgresql://youruser@localhost:5432/late_show_db
   JWT_SECRET_KEY=supersecretkey
   

3. **Set Up the Database**

   Create a PostgreSQL database named `late_show_db`:

   
   sudo -u postgres psql
   CREATE DATABASE late_show_db;
   \q
   

4. **Initialize and Migrate the Database**

   
   export FLASK_APP=server/app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   

5. **Seed the Database**

   
   python server/seed.py
   

6. **Start the Server**

   
   flask run
   

   The app will run on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

7. **Test with Postman**

   Import the included `challenge-4-lateshow.postman_collection.json` into Postman and test the following routes:

   | Route                  | Method | Auth Required? | Description                          |
   |------------------------|--------|----------------|--------------------------------------|
   | `/register`            | POST   | ❌             | Register a user                      |
   | `/login`               | POST   | ❌             | Log in + return JWT                 |
   | `/episodes`            | GET    | ❌             | List episodes                        |
   | `/episodes/<int:id>`   | GET    | ❌             | Get episode + appearances           |
   | `/episodes/<int:id>`   | DELETE | ✅             | Delete episode + appearances        |
   | `/guests`              | GET    | ❌             | List guests                          |
   | `/appearances`         | POST   | ✅             | Create appearance                    |

   ⚠️ For protected routes (DELETE/POST), first log in and ensure the `Authorization` header is set:
   ```http
   Authorization: Bearer <your-token>
   

---

## ✅ Notes

- Ensure PostgreSQL is running locally.
- Use `pipenv shell` to activate the environment before running commands.
- JWT tokens expire after a short time for security. Always log in again if the token expires.
- Don't forget to add `.env` to your `.gitignore`.



