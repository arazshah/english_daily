from datetime import datetime
from app import db


class Word:
    @staticmethod
    def get_word_of_the_day():
        today = datetime.today().date()
        word_data = db.words.find_one({'date': today.isoformat()})
        if not word_data:
            word_data = {
                'word': 'Example',
                'image1': 'https://via.placeholder.com/150',
                'image2': 'https://via.placeholder.com/150',
                'image3': 'https://via.placeholder.com/150',
                'image4': 'https://via.placeholder.com/150',
                'sentence1': 'This is sentence 1.',
                'sentence2': 'This is sentence 2.',
                'sentence3': 'This is sentence 3.',
                'context': 'This is the context of the word.',
                'audio': 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
                'video': 'https://www.w3schools.com/html/mov_bbb.mp4',
                'date': today.isoformat()
            }
            db.words.insert_one(word_data)
        return word_data

    @staticmethod
    def get_all():
        return list(db.words.find())

    @staticmethod
    def create(word_data):
        db.words.insert_one(word_data)

    @staticmethod
    def update(word_id, word_data):
        db.words.update_one({'_id': word_id}, {'$set': word_data})

    @staticmethod
    def delete(word_id):
        db.words.delete_one({'_id': word_id})
