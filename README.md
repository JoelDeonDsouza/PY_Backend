
# User Management API

This Flask application provides a simple API for managing users including creating, retrieving, updating, and deleting user records in a database.

## Installation

```bash
https://github.com/JoelDeonDsouza/PY_Backend.git
```

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up the database configuration in the `config.py` file.
4. Run the application using `python main.py || python3 main.py`.

## Usage

### Get Users
- **Endpoint:** `/users`
- **Method:** `GET`
- **Description:** Retrieves a list of all users stored in the database.
- **Response:** Returns a JSON object containing the list of users.

### Create User
- **Endpoint:** `/create_user`
- **Method:** `POST`
- **Description:** Creates a new user record in the database.
- **Request Body:** Requires a JSON object with `name` and `email` fields.
- **Response:** Returns a success message if the user is created successfully.

### Update User
- **Endpoint:** `/update_user/<user_id>`
- **Method:** `PATCH`
- **Description:** Updates an existing user record in the database.
- **Parameters:** Requires the `user_id` of the user to be updated.
- **Request Body:** Accepts a JSON object with optional `name` and `email` fields to be updated.
- **Response:** Returns a success message if the user is updated successfully.

### Delete User
- **Endpoint:** `/delete_user/<user_id>`
- **Method:** `DELETE`
- **Description:** Deletes an existing user record from the database.
- **Parameters:** Requires the `user_id` of the user to be deleted.
- **Response:** Returns a success message if the user is deleted successfully.

## Running the Application

To run the application, execute `python main.py || python3 main.py` in your terminal. By default, the application runs in debug mode.

## Note

Make sure to set up the database configuration in the `config.py` file before running the application.

```python
# config.py

app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'