# Kwitter

Welcome to the Kwitter project repository! This project is a web application that allows users to create, edit, delete, and view posts (Kweets). The project is built using Django for the backend and includes various functionalities for user authentication and CRUD operations on Kweets.

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Libraries and Modules](#libraries-and-modules)
3. [Project Setup](#project-setup)
   - [Creating a Virtual Environment](#creating-a-virtual-environment)
   - [Installing Dependencies](#installing-dependencies)
4. [Running the Application](#running-the-application)
5. [Contributing](#contributing)
6. [License](#license)

## Technologies Used

- **Django**: Web framework used for building the backend of the application.
- **Bootstrap 5**: CSS framework for styling and responsive design.
- **SQLite**: Database engine used for local development.
- **HTML/CSS**: Markup and styling languages for front-end development.

## Libraries and Modules

- **Django**: The main web framework used for building the project.
- **Gunicorn**: WSGI HTTP server for running the Django application in production.
- **Pillow**: Image processing library used for handling image uploads.
- **sqlparse**: Library for parsing SQL statements.
- **tzdata**: Time zone data for accurate time representation.
- **django-extensions**: Provides additional management commands and features for Django development.
- **asgiref**: ASGI (Asynchronous Server Gateway Interface) library used for Django’s ASGI support.

## Project Setup

### Creating a Virtual Environment

1. **Navigate to the project directory**:
    ```bash
    cd path/to/your/project
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source env/bin/activate
      ```

### Installing Dependencies

1. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Create a `.env` file** (if not already provided) in the root directory of the project and add the following lines:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

   Replace `your_secret_key` with a secure key for your Django project.

## Running the Application

1. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

2. **Create a superuser** (for admin access):
    ```bash
    python manage.py createsuperuser
    ```

3. **Collect static files**:
    ```bash
    python manage.py collectstatic
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

   Access the application in your web browser at `http://localhost:8000`.

5. **Running in Production**:

   To run the application in production, use Gunicorn:

    ```bash
    gunicorn kwitter.wsgi:application
    ```

   This command will start Gunicorn, which will serve the Django application.

## Contributing

We welcome contributions to enhance the project. Here are a few tasks you can work on:

1. **CSS Styling**: Improve the CSS styling of the application. Currently, basic styles are applied. You can enhance the look and feel by adding more detailed and responsive styles.

   - Modify `static/css/style.css` for custom styles.
   - Ensure styles are consistent across different screen sizes.

2. **Feature Enhancements**: Add new features or improve existing ones. For example, you might want to implement additional functionalities or improve user experience.

3. **Bug Fixes**: Report and fix any bugs you encounter. Ensure to test thoroughly after making changes.

To contribute, please fork the repository, make your changes in a separate branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
