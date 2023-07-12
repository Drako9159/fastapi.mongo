This is the README for the project developed by @drako9159. Below you will find information about the application, the technologies used, and how to run it.

## Project Description

The project is a backend application built using FastAPI and MongoDB. It is a simple application designed to test the mentioned libraries and apply a virtual environment (venv). A task model and its CRUD operations have been implemented.

## Technologies Used

The project utilizes the following technologies and libraries:

- FastAPI: A modern, fast web framework for building APIs with Python.
- MongoDB: A document-oriented NoSQL database.
- Uvicorn: A high-performance ASGI server used to run the application.
- Motor: An asynchronous MongoDB driver for asyncio.

## Environment Setup

To run the application, it is recommended to follow the steps below:

1. Clone the project repository.
2. Create a virtual environment (venv) using your preferred tool.
3. Activate the newly created virtual environment.
4. Install the required dependencies by running the following command:

``````cmd
pip install -r requirements.txt
uvicorn app.main:app --reload
``````
5. Ensure you have a running instance of MongoDB. It can be local or remote. Update the connection configuration in the `app/main.py` file if necessary.
6. Run the development server using the following command:

7. The application will be available at `http://localhost:8000`. You can explore the different routes using a tool like Postman or through a web browser.

## Project Structure

The project follows the following directory structure:


.
├── app
│ ├── crud
│ ├── db
│ ├── models
│ ├── routes
│ └── main.py
├── .gitignore
└── requirements.txt


- The `app` directory contains the different modules of the application.
- The `crud` directory includes files related to the CRUD operations of the task model.
- The `db` directory contains the database connection configuration.
- The `models` directory defines the data structure of the task model.
- The `routes` directory contains the application's routing files.
- The `.gitignore` file specifies the files and directories to be ignored by Git.
- The `requirements.txt` file lists the project dependencies.

Feel free to explore and modify the code as needed to fit your requirements.

Enjoy using the application and developing with FastAPI and MongoDB! If you have any questions or concerns, don't hesitate to contact @drako9159.
