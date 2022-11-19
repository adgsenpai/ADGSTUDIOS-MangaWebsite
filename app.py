#!/usr/bin/env python3


### Importing Modules, Files, etc.
from flask import (
    Flask,
    render_template,
    url_for,
    request,    
    session
)
from werkzeug.exceptions import HTTPException
from flask_session import Session
from helper.manga_page import *
from helper.search import SearchEngine, RandomAnimeGif


### Creating App Object
app = Flask(__name__)

#set the secret key.  keep this really secret:
app.secret_key = 'mySuperSecretKey'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
Session(app)


### Routing
# Home Page with search Engine
@app.route("/")
def homePage():
    query = request.args.get('search')
    if query is not None:
        if query:
            search = SearchEngine(query)
            return render_template('search.html', result = search.mangaList, contextname="Search", pagename='Search Results for ' + query)
        
    gif = RandomAnimeGif()
    return render_template('index.html', gifUrl = gif.imgUrl,contextname="マンガ@アドグストゥディオズ",pagename="Homepage")

# About Page
@app.route("/about")
def aboutPage():
    return render_template('about.html')

# Contact Page
@app.route("/contact")
def contactPage():
    return render_template('contact.html')

# Chapter List of Manga
@app.route("/manga/<string:manga_id>")
def chapterList(manga_id):                                                        
    chap = Chapter(manga_id)
    session['manga_id'] = manga_id
    session['mangatitle'] = chap.title    
    return render_template(
        'manga.html',
        mangaid= manga_id,
        manga_title= chap.title,
        chapList = chap.chapJson,
        title = chap.title,
        poster = chap.posterUrl,
        description = chap.description,
        genre = chap.genre,
        rating = chap.rating,
        contextname=chap.title,
        pagename="Chapter List"
    )

# Pages of Manga
@app.route('/chapters/<int:chapter_id>')
def chapterPages(chapter_id):
    pge = ChapterPage(chapter_id,session['manga_id'])
 
    return render_template(
        'manga_page.html',
        pageData = pge.pageList,
        manga_title = str(session.get('mangatitle')),
        mangaid= session['manga_id'], 
        pagename = pge.chapterTitle,       
        prevLink = pge.previousChapter,
        nextLink = pge.nextChapter,
        previousChapName = pge.previousChapName,
        nextChapName = pge.nextChapName,

    )

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("error.html", e=e, contextname="Error", pagename="Error"), 500

#not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template("notfound.html", e=e, contextname="404", pagename="Page Not Found"), 404

### Running Web
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)

