import requests
import random

def fetch_text():
    paras = random.randint(2,3)
    url = f"https://baconipsum.com/api/?type=meat-and-filler&paras={paras}"
    response = requests.get(url)
    return "\n\n".join(response.json())

def calculate_wpm(text, time_taken):
    words = len(text.split())
    minutes = time_taken / 60
    return round(words / minutes, 2)

def calculate_accuracy(original, typed):
    correct = 0
    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1
    return round((correct / len(original)) * 100, 2)
