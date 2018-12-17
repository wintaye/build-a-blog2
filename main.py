from flask import Flask, request, redirect, render_template, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog2:password@localhost:8889/build-a-blog2'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'a;slkfjalskdfjl;aksdfj;alksdfjl;askdf'

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.String(1500))
    created = db.Column(db.DateTime)

    def __init__(self, title, body, created=None):
        self.title = title
        self.body = body
        if created is None:
            created = datetime.utcnow()
        self.created = created

    def is_valid(self):
        if self.title and self.body and self.created:
            return True
        else:
            return False

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect("/blog")

@app.route("/blog", methods=['GET', 'POST'])
def display_blog_posts():
    #display all posts or new blog post page
    blog_id = request.args.get('id')
    if blog_id:
        blog = Blog.query.get(blog_id)
        #blog = Blog.query.order_by(blog_id.desc()).all()
        return render_template('single_post.html', title="New Blog Post", blog=blog)
    else:  
        all_blog_posts = Blog.query.all()
        return render_template('all_blog_posts.html', title="All Blog Entries", all_blog_posts=all_blog_posts)


@app.route('/new_post')
def make_new_post():
    return render_template('new_post_form.html')

@app.route("/new_post", methods=['POST'])
def new_entry():
    #add new blog post to db
    if request.method == 'POST':
        new_blog_title = request.form['title']
        new_blog_body = request.form['body']
        new_blog_post = Blog(new_blog_title, new_blog_body)
        if new_blog_post.is_valid():
            db.session.add(new_blog_post)
            db.session.commit()
            url = "/blog?id=" + str(new_blog_post.id)
            return redirect(url)
        else:
            flash("Please check your entry for errors. Both a post title + body are required.")
            return render_template('new_post_form.html', title="Create a new blog post", new_blog_title=new_blog_title, new_blog_body=new_blog_body)

if __name__=='__main__':
    app.run()

