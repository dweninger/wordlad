from django.shortcuts import render
import requests
import random
from django.http import JsonResponse

#WordLad

start_words = [
    'back', 'fool', 'mind', 'high', 'hold', 'reel',
    'fuel', 'watt', 'warm', 'with', 'game', 'gold',
    'cows', 'rock', 'spur', 'slam', 'debt', 'stay',
    'fist', 'cold', 'lies', 'play', 'shoe', 'alum',
    'true', 'done', 'yoga', 'sore', 'join', 'help',
    'vote', 'rain', 'mold', 'very', 'jury', 'scar',
    'star', 'open', 'keep', 'ouch', 'poor', 'wolf',
    'about', 'brush', 'light', 'music', 'stone', 'cloud',
    'quick', 'plant', 'laugh', 'bread', 'night', 'heart'
    ]
end_words = [
    'door', 'jest', 'game', 'jump', 'fast', 'spin',
    'tank', 'volt', 'milk', 'hold', 'code', 'leaf',
    'milk', 'band', 'barb', 'dunk', 'loan', 'here',
    'bump', 'brew', 'fact', 'ball', 'foot', 'grad',
    'love', 'deal', 'pose', 'head', 'team', 'desk',
    'veto', 'pour', 'clay', 'much', 'seat', 'face',
    'gaze', 'mind', 'sake', 'hurt', 'rich', 'howl',
    'house', 'paint', 'flame', 'notes', 'rocks', 'storm',
    'swift', 'trees', 'smile', 'toast', 'sleep', 'organ'
    ]
optimal_turns = [
    4, 5, 4, 6, 4, 5,
    5, 4, 4, 5, 3, 4,
    4, 4, 6, 6, 5, 5,
    5, 4, 5, 5, 3, 4,
    6, 4, 4, 5, 5, 4,
    5, 5, 5, 6, 6, 6,
    6, 6, 6, 6, 5, 3,
    10, 5, 10, 6, 6, 6,
    9, 6, 6, 7, 9, 10
    ]

def wordlad(request):
    rand_index = random.randint(0,len(start_words) - 1)
    return render_wordlad(request, rand_index)

def wordlad_number(request, wordlad_number):
    return render_wordlad(request, wordlad_number - 1)
    
def render_wordlad(request, wordlad_number):
    keyboard_top = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',' p']
    keyboard_mid = ['a', 's', 'd', 'f','g', 'h', 'j', 'k', 'l']
    keyboard_bot = ['Enter', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Del']
    
    context = {
        'wordlad_index': wordlad_number + 1,
        'total_wordlads': len(start_words),
        'start_word': start_words[wordlad_number],
        'end_word': end_words[wordlad_number],
        'optimal_turns': optimal_turns[wordlad_number],
        'keyboard_top': keyboard_top,
        'keyboard_mid': keyboard_mid,
        'keyboard_bot': keyboard_bot,
    }
    return render(request, 'wordlad.html', context)

def word_exists(request, word):
    api_endpoint = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(api_endpoint)
    return JsonResponse({'exists': response.status_code == 200})
