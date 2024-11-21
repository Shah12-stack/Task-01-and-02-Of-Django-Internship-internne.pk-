from django.shortcuts import render
from django.http import HttpResponse

def introduce_yourself(request):
    # Simple introduction data
    intro_data = {
        'name': 'Muhammad Shahzaman Khan',
        'age': 21,
        'profession': 'Software Developer',
        'hobbies': 'Cricket, Coding, Movies, Reading',
        'message': 'Hello! Iam  Muhammad Shahzaman Khan, a passionate software developer with a strong interest in web development, including technologies like Python, Django, WordPress, and JavaScript. I thrive on solving problems and constantly learning new skills through hands-on projects. Outside of coding, I enjoy playing cricket, photography, and staying active, aiming for a balanced life where creativity and technical expertise go hand in hand.'
    }
    return render(request, 'introduction/introduction.html', intro_data)
