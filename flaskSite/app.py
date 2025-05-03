from forms import ArticleForm
from flask import Flask, render_template, request, url_for , redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key'  # CSRF protection key

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    intro = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(100))

    def __repr__(self):
        return f"('{self.id}', '{self.title}', '{self.date_created}')"

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')
        
@app.route('/create_article', methods=['GET', 'POST'])
def create_article():
    form = ArticleForm()
    if form.validate_on_submit():
        title = form.title.data
        intro = form.intro.data
        text = form.text.data

        image_file = form.image.data
        if image_file:
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
        else:
            filename = 'default.jpg'

        new_article = Article(title=title, intro=intro, text=text, image=filename)
        try:
            db.session.add(new_article)
            db.session.commit()
            return redirect(url_for('articles'))
        except:
            return "There was an issue adding your article"
    return render_template('create_article.html', form=form)

@app.route('/articles')
def articles():
    articles = Article.query.order_by(desc(Article.date_created)).all()
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article_detail.html', article=article)


if __name__ == '__main__':
    app.run(debug=True)