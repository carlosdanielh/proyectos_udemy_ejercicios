#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
from pathlib import Path

# The quiz data. Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}


def header():
    quiz.Write('Unidad Educativa Martin Lutero\n')
    quiz.write('Fechas:\n')
    quiz.write('Nombre:\n')
    quiz.write('Los estados de cada ciudad de los Estados Unidos:\n')
    quiz.write('Seleccione la respuesta correcta:\n')
    quiz.write('________________________________________________'


# list_of_all_capitals = list(capitals.values())
# Generate 35 quiz files.
for quizNum in range(2):
    # TODO: Create the quiz and answer key files.
    with open(str(Path.cwd() / 'udemy_projects' / 'files_boringstuff'
              / 'quizes' / f'file_{quizNum}_quiz.txt'), 'r') as quiz:
        # TODO: Write out the header for the quiz.
        # header()
        # TODO: Shuffle the order of the states.
        random.choice(list_of_all_capitals)
        # TODO: Loop through all 50 states, making a question for each.
        # aquiz.write(f'#{quizNum} - ')
