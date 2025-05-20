📄 Description:
This is a dynamic web application built using Django (Python Web Framework), integrated with HTML, CSS, and JavaScript for a responsive frontend experience. The project is structured with a clear separation of templates and static files, ensuring maintainability and scalability.

🌐 Key Features:
🔷 Multi-page Interface:

index.html: Home page with an overview.

about.html: Provides information about the website or organization.

form.html: A user data collection form (Name, Age, Address, Mobile, Email).

contact.html: Contact form for user queries (Name, Email, Message).

🎨 Frontend Design:

Clean and responsive UI using HTML5 and CSS3.

Interactive elements powered by Vanilla JavaScript.

🧠 Backend with Django:

URL routing and view management for smooth navigation.

Data validation and redirection upon form submission.

🗃️ Database Integration:

SQLite (db.sqlite3) used as the backend database.

Stores user input from both Form Page and Contact Us Page securely.

Models defined in myaap/models.py and integrated via Django ORM.

📨 Form Handling:

Input fields are captured using Django forms/views.

Data is saved to the database, and the user is redirected to the homepage.

📂 Static & Template Management:

All HTML files placed under the templates directory.

CSS and JavaScript files stored under the static directory for easy asset management.

🧰 Technologies Used:
Django (Python)

HTML

CSS

JavaScript 

SQLite3 (default Django database)

📌 How to Run:
Clone the repository.

Navigate to the project directory.

Run python manage.py runserver.

Access the application at http://127.0.0.1:8000/
