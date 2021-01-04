sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split(' ')

dictionary_count = {key : len(key) for key in sentence_list}

print(dictionary_count)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

new_dict = {key : round((value * 1.8), 2) + 32 for key,value in weather_c.items()}

print(new_dict)