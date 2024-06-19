from django.core.management.base import BaseCommand
from keras.models import load_model
import pickle
import json


class Command(BaseCommand):
    help = 'Load the trained chatbot model'

    def handle(self, *args, **kwargs):
        self.model = load_model('chatbot_app/chatbot_model.h5')
        self.words = pickle.load(open('chatbot_app/words.pkl', 'rb'))
        self.classes = pickle.load(open('chatbot_app/classes.pkl', 'rb'))
        self.intents = json.loads(open('chatbot_app/intents.json').read())
        self.stdout.write(self.style.SUCCESS('Model loaded successfully'))
