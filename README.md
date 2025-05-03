# Elektric OÜ Website

This is a Flask-based web application for Elektric OÜ, a professional electrical services company. The website provides information about the company, its services, and allows users to create and view articles.

## Features

- **Home Page**: A hero section with a call-to-action button and an introduction to Elektric OÜ.
- **About Page**: Information about the company's mission and team.
- **Services Page**: Details about the residential, commercial, and industrial services offered.
- **Contact Page**: Contact information and address.
- **Articles**: A section to view all articles, create new articles, and view article details.
- **Responsive Design**: Fully responsive layout using Bootstrap 5.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite
- **Forms**: Flask-WTF
- **File Uploads**: Flask-WTF with image upload support

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/qannje/elektric-ou-website.git
   cd elektric-ou-website```
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows```

3. Install the required dependencies
 ```bash
   pip install -r requirements.txt
```
   
4. Create the SQLite database
   (The instance/ folder is used to store the SQLite database.
   It is intentionally empty in the repository.
   A new database will be created there when you run the code.):
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()```

6. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to:
```bash
http://127.0.0.1:5000
```
Project Structure
```bash
flaskSite/
├── static/
│   ├── style.css
│   ├── uploads/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── services.html
│   ├── articles.html
│   ├── article_detail.html
│   ├── create_article.html
├── app.py
├── forms.py
├── site.db
```
## Screenshots
[Home page](images/elektric-ou-homepage.png)
[Create Article page](images/elektric-ou-create_aricle.png)


## Future Enhancements\
- Add article edit/delete function.
- Add user authentication for article creation.
- Implement pagination for the articles page.
- Add a search feature for articles.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contribute to this project by submitting issues or pull requests!
