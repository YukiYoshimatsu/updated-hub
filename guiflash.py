
from random import randint
from Tkinter import *
from collections import OrderedDict

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

widge = Tk()
widge.geometry('200x200')
class vocabulary_Lesson():
  # Displays a list of spanish words and their english translation
   def __init__(self, subject, contents):
       self.sub = subject
       self.con = contents
      # subject refers to an entry made in the vocabulary tuple


   def print_Subject(self):
       lbl = Label(widge,text='This unit\'s topic is: ' + self.sub)
       lbl.grid(column=0,row=4)

   def display_Contents(self):
       for key in self.con:
           lbl2= Label(widge,text=key + " => " + self.con[key])
           lbl2.grid(column=0,row=6)

   def start_Flashcards(self):
       lbl3 = Label(widge,text='Please enter the number of the mode of practice: \n1: Spanish to English \n2: English to Spanish \n3: Mixed')
       lbl3.grid(column=0,row=8)
       print ("Before input")
       mode = input()
       tries = 0  # tries tracks the amount of incorrect guesses
       print ("After mode")
       if ((mode != 1) and (mode != 2) and (mode != 3)):
           lbl4= Label(widge,text='Error: Please enter a valid number for the mode of practice:')
           lbl4.grid(column=0,row=10)
           self.start_Flashcards()

       elif (mode == 1):
           tries = 0
           for key in self.con:
               lbl5= Label(widge,text=key)
               lbl5.grid(column=0,row=12)
               lbl6= Label(widge,text='Please enter the English translation of the above word: ')
               lbl6.grid(column=0,row=14)
               response = raw_input()
               if (response.lower() != self.con[key].lower()):
                   tries = tries + 1
                   sec_response = raw_input('Incorrect, please try again.\n')
                   if (sec_response.lower() != self.con[key].lower()):
                       tries = tries + 1
                       lbl7= Label(widge,text='Incorrect, the correct answer is: ' + self.con[key])
                       lbl7.grid(column=0,row=16)
           lbl8= Label(widge,text='You have passed through ' + str(len(self.con)) + ' words with ' + str(tries) + ' error(s).')
           lbl8.grid(column=0,row=18)

       elif (mode == 2):
           tries = 0
           for key in self.con:
               Label(self.con[key])
               Label('Please enter the Spanish translation of the above word: ')
               response = raw_input()
               if (response.lower() != key.lower()):
                   tries = tries + 1
                   sec_response = raw_input('Incorrect, please try again.\n')
                   if (sec_response.lower() != key.lower()):
                       tries = tries + 1
                       Label('Incorrect, the correct answer is: ' + key)
           Label('You have passed through ' + str(len(self.con)) + ' words with ' + str(tries) + ' error(s).')

          # mixed Spanish and English
       elif (mode == 3):
           tries = 0
           for key in self.con:
               determiner = randint(0, 1)
               if (determiner == 0):
                   Label(self.con[key])
               else:
                   Label(key)
               Label('Please enter the translation of the above word: ')
               sec_response = raw_input()
               if (((determiner != 0) and (sec_response.lower() != self.con[key].lower())) or (
                      (determiner != 1) and (sec_response.lower() != key.lower()))):
                   tries = tries + 1
                   sec_response = raw_input('Incorrect, please try again.\n')
                   if (((determiner != 0) and (sec_response.lower() != self.con[key].lower())) or (
                          (determiner != 1) and (sec_response.lower() != key.lower()))):
                       tries = tries + 1
                       print ('Incorrect, the correct answer is: ' + key + ' <-> ' + self.con[key])
           Label('You have passed through ' + str(len(self.con)) + ' words with ' + str(tries) + ' error(s).')


class grammer_Lesson():

   def __init__(self, subject):
       self.sub = subject

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

school = vocabulary_Lesson('Activity', words_Activities)
print("Before Display Contents......")
school.display_Contents()
print("Before Print Subject....")
school.print_Subject()
print("Before Greeting")
greetings = vocabulary_Lesson('Society', words_Society)
school.start_Flashcards()
print("After Flashcards")
widge.mainloop()
