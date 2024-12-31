from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.word import Word
from app.utils.decorators import admin_required


@admin_required
def admin():
    words = Word.get_all()
    return render_template('admin/admin.html', words=words)


@admin_required
def add_word():
    if request.method == 'POST':
        word_data = {
            'word': request.form['word'],
            'image1': request.form['image1'],
            'image2': request.form['image2'],
            'image3': request.form['image3'],
            'image4': request.form['image4'],
            'sentence1': request.form['sentence1'],
            'sentence2': request.form['sentence2'],
            'sentence3': request.form['sentence3'],
            'context': request.form['context'],
            'audio': request.form['audio'],
            'video': request.form['video'],
            'date': request.form['date']
        }
        Word.create(word_data)
        flash('Word added successfully!', 'success')
        return redirect(url_for('admin'))
    return render_template('admin/add_word.html')


@admin_required
def edit_word(word_id):
    word = Word.get(word_id)
    if request.method == 'POST':
        word_data = {
            'word': request.form['word'],
            'image1': request.form['image1'],
            'image2': request.form['image2'],
            'image3': request.form['image3'],
            'image4': request.form['image4'],
            'sentence1': request.form['sentence1'],
            'sentence2': request.form['sentence2'],
            'sentence3': request.form['sentence3'],
            'context': request.form['context'],
            'audio': request.form['audio'],
            'video': request.form['video'],
            'date': request.form['date']
        }
        Word.update(word_id, word_data)
        flash('Word updated successfully!', 'success')
        return redirect(url_for('admin'))
    return render_template('admin/edit_word.html', word=word)


@admin_required
def delete_word(word_id):
    Word.delete(word_id)
    flash('Word deleted successfully!', 'success')
    return redirect(url_for('admin'))
