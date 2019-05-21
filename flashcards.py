from random import randint
from tkinter import *

lessons = ('basic vocab', 'gender of words', 'demonstrative', 'word order agreement',
           'present tense & irregulars/stem changers', 'ser vs estar',
           'posessive pronouns', 'reflexive verbs', 'verbs like gustar',
           'gerund & progressive', 'adverbs', 'superlatives', 'preterite & car,gar,zar', 'imperfect',
           'hacer/past participle', 'conditional & irregulars', 'passive voice',
           'impersonal se', 'commands', 'present perfect', 'subjunctive')

vocabulary = ('school work', 'greetings & personal info', 'descriptions', 'numbers', 'family',
              'health', 'class subjects', 'hobbies', 'routines', 'navigation',
              'art', 'science & technology', 'medical', 'society', 'government',
              'nature', 'activities')


class vocabulary_Lesson():
    # Displays a list of spanish words and their english translation
    def __init__(self, subject, contents):
        self.sub = subject
        self.con = contents
        # subject refers to an entry made in the vocabulary tuple

    def print_Subject(self):
        print ('This unit\'s topic is: ' + self.sub)

    def display_Contents(self):
        for key in self.con:
            print (key + " => " + self.con[key])

    def start_Flashcards(self):
        print (
            'Please enter the number of the mode of practice: \n1: Spanish to English \n2: English to Spanish \n3: Mixed')
        mode = input()
        tries = 0  # tries tracks the amount of incorrect guesses
        if ((mode != 1) and (mode != 2) and (mode != 3)):
            print ('Error: Please enter a valid number for the mode of practice:')
            self.start_Flashcards()

        elif (mode == 1):
            tries = 0
            for key in self.con:
                print (key)
                print ('Please enter the English translation of the above word: ')
                response = raw_input()
                if (response.lower() != self.con[key].lower()):
                    tries = tries + 1
                    sec_response = raw_input('Incorrect, please try again.\n')
                    if (sec_response.lower() != self.con[key].lower()):
                        tries = tries + 1
                        print ('Incorrect, the correct answer is: ' + self.con[key])
            print ('You have passed through ' + str(len(self.con)) + ' words with ' + str(tries) + ' error(s).')

        elif (mode == 2):
            tries = 0
            for key in self.con:
                print (self.con[key])
                print ('Please enter the Spanish translation of the above word: ')
                response = raw_input()
                if (response.lower() != key.lower()):
                    tries = tries + 1
                    sec_response = raw_input('Incorrect, please try again.\n')
                    if (sec_response.lower() != key.lower()):
                        tries = tries + 1
                        print ('Incorrect, the correct answer is: ' + key)
            print ('You have passed through ' + str(len(self.con)) + ' words with ' + str(tries) + ' error(s).')

            # mixed Spanish and English
        elif (mode == 3):
            tries = 0
            for key in self.con:
                determiner = randint(0, 1)
                if (determiner == 0):
                    print (self.con[key])
                else:
                    print (key)
                print ('Please enter the translation of the above word: ')
                sec_response = raw_input()
                if (((determiner != 0) and (sec_response.lower() != self.con[key].lower())) or (
                        (determiner != 1) and (sec_response.lower() != key.lower()))):
                    tries = tries + 1
                    sec_response = raw_input('Incorrect, please try again.\n')
                    if (((determiner != 0) and (sec_response.lower() != self.con[key].lower())) or (
                            (determiner != 1) and (sec_response.lower() != key.lower()))):
                        tries = tries + 1
                        print ('Incorrect, the correct answer is: ' + key + ' <-> ' + self.con[key])
            print ('You have passed through ' + str(len(self.con)) + ' words with ' + str(tries) + ' error(s).')


class grammer_Lesson():

    def __init__(self, subject):
        self.sub = subject

from collections import OrderedDict
#Vocabulary lesson topics and dictionaries
words_School_Work = OrderedDict([('Tarea', 'Homework'), ('Libro', 'Book')])
words_Greetings = {}
words_Descriptions = {}
words_Numbers = {}
words_Family = {}
words_Health = {}
words_Class_Subjects = {}
words_Hobbies = {}
words_Routines = {}
words_Navigation = {}
words_Art = {}
words_Science_Tech = {}
words_Medical = OrderedDict([('Adolorido', 'In Pain'), ('Cirugia', 'Surgery'), ('Contagioso', 'Contagious'),
                             ('Diagnosticar', 'To diagnose'), ('Efectos adversos', 'Adverse effects'),
                             ('Embarazo', 'Pregnancy'), ('Fiebre', 'Fever'), ('Epidemia', 'Epidemic'),
                             ('Gripe', 'Flu'), ('Hierbas medicionales', 'Medicinal herbs'), ('higiene', 'Hygene'),
                             ('Hinchar', 'To swell'), ('influenza', 'Influenza'), ('Insomnio', 'Insomnia'),
                             ('Medicinas alternativas', 'Alternative medicines'), ('Microbios', 'Germs'),
                             ('Obesida', 'Obesity'), ('Paciente', 'Patient'), ('Padecer de', 'To suffer from'),
                             ('Pastillas', 'Pills'), ('Receta', 'Prescription'), ('Resfriado', 'A cold'),
                             ('saludable', 'Healthy(for you)'), ('Sano', 'Healthy'), ('Sindrome', 'Syndrome'),
                             ('Sobrepeso', 'Overweight'), ('terapia', 'therapy'), ('tratamientos', 'treatments')])

words_Society = OrderedDict([('Amistad', 'Friendship'), ('Ancianos', 'Elderly'), ('Avances', 'Advamcements'),
                             ('Calidad de vida', 'Quality of life'), ('Caridad', 'Charoty'), ('Crimen', 'Crime'),
                             ('Derechos humanos', 'Human rights'), ('Desigualdad', 'Inequality'),
                             ('Desplazados', 'Desplaced'), ('Discapacidad', 'Disabled'), ('Pobreza', 'Poverty'),
                             ('Refugio politico', 'Polical asylum'), ('Sanidad', 'Health'), ('Seguridad', 'Security'),
                             ('Viuda', 'Widow')])

words_Nature = OrderedDict([('Ambiente', 'Atmosphere'), ('Calentamiento global', 'Global warming'),
                            ('Capa de ozono', 'Ozone layer'), ('Combustibles', 'Fuel'), ('Derretimiento', 'Melting'),
                            ('Desechos', 'Wastes'), ('Efecto invernadero', 'Greenhouse effect'), ('Entorno', 'Environment'),
                            ('Extinguirse', 'To become extinct'), ('Glaciar', 'glacier'), ('Huella de carbono', 'Carbon footprint'),
                            ('Masa polar', 'Polar ice cap'), ('Petroleo', 'Oil'), ('Placas', 'Plates'), ('Reciclaje', 'Recycling'),
                            ('Reciclar', 'to recycle'), ('Recursos', 'Resources'), ('Recursos renovables', 'Renewable resources')])
words_Activities = OrderedDict([('Balancesto', 'Basketball'), ('Escalar', 'To climb(mountain)')])

school = vocabulary_Lesson('Nature', words_Nature)
school.display_Contents()
school.print_Subject()
greetings = vocabulary_Lesson('Nature', words_Nature)
school.start_Flashcards()


