
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
words_Government = {}
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
greetings = vocabulary_Lesson('Society', words_Society)
school.start_Flashcards()
