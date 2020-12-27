#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
import random
from pathlib import Path

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
    quiz.write('Unidad Educativa Martin Lutero\n')
    quiz.write('Fechas:\n')
    quiz.write('Nombre:\n')
    quiz.write('Los estados de cada ciudad de los Estados Unidos:\n')
    quiz.write('Seleccione la respuesta correcta:\n')
    quiz.write('________________________________________________\n')


def display_the_correct_answer_with_three_wrong_answer(city):

    has_load_all_list = False
    while not has_load_all_list:
        list_state_to_display = []
        list_state_to_display.append(capitals[city])

        for _ in range(3):
            state = random.choice(list_of_all_states)
            list_state_to_display.append(state)

        new_list_state = list(set(list_state_to_display))
        if len(new_list_state) == 4:
            random.shuffle(list_state_to_display)
            for state in list_state_to_display:
                quiz.write(f'( ) {state}\n')
            has_load_all_list = True
        else:
            has_load_all_list = False


def unordered_city_list(dictionary):
    city_list = list(dictionary)
    random.shuffle(city_list)
    return city_list


list_of_all_states = list(capitals.values())
for quizNum in range(2):
    the_path = (Path.cwd() / 'udemy_projects' / 'files_boringstuff'
                / 'quizes' / f'file_{quizNum + 1}_quiz.txt')
    with open(str(the_path), 'w') as quiz:
        header()
        for num, city in enumerate(unordered_city_list(capitals)):
            quiz.write(f'#{num + 1}-Wich is the capital '
                       f'of {city} \n')
            display_the_correct_answer_with_three_wrong_answer(city)
