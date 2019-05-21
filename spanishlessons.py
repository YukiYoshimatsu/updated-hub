lessons = ('basic vocab', 'gender of words', 'demonstrative', 'word order agreement',
           'present tense & irregulars/stem changers', 'ser vs estar',
           'posessive pronouns', 'reflexive verbs', 'verbs like gustar',
           'gerund & progressive', 'adverbs', 'superlatives', 'preterite', 'imperfect',
           'hacer/past participle', 'conditional & irregulars', 'passive voice',
           'impersonal se', 'commands', 'present perfect', 'subjunctive')

vocabulary = ('school work', 'greetings & personal info', 'descriptions', 'numbers', 'family',
              'health', 'class subjects', 'hobbies', 'routines', 'navigation',
              'art', 'science & technology', 'medical', 'society', 'government',
              'nature', 'activities')


class vocabulary_Display():
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




#Vocabulary lesson topics and dictionaries
words_School_Work = {'tarea': 'homework', 'libro': 'book'}
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
words_Medical = {}
words_Society = {}
words_Government = {}
words_Nature = {}
words_Activities = {}

school = vocabulary_Display('School Work', words_School_Work)
school.display_Contents()
school.print_Subject()
greetings = vocabulary_Display('Greetings & Personal information', words_Greetings)