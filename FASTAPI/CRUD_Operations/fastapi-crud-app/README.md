# FastAPI CRUD App

This project is a simple FastAPI application that implements CRUD (Create, Read, Update, Delete) operations and uses an SQLite3 database for data storage.

## Project Structure

```
fastapi-crud-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-crud-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- **Create**: `POST /items/` - Create a new item.
- **Read**: `GET /items/` - Retrieve all items.
- **Read**: `GET /items/{item_id}` - Retrieve a specific item by ID.
- **Update**: `PUT /items/{item_id}` - Update a specific item by ID.
- **Delete**: `DELETE /items/{item_id}` - Delete a specific item by ID.

## License

This project is licensed under the MIT License.