from flask import render_template
from flask_login import login_required
from app.models.word import Word


@login_required
def training():
    word_of_the_day = Word.get_word_of_the_day()
    return render_template('training/training.html', word=word_of_the_day)
