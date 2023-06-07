from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main import *

zodiac_dict = (Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces)
fire = [i for i in zodiac_dict if i.att == 'fire']
earth = [i for i in zodiac_dict if i.att == 'earth']
air = [i for i in zodiac_dict if i.att == 'air']
water = [i for i in zodiac_dict if i.att == 'water']

def index(request, type_zd=zodiac_dict, ul=False):
    li_elements = ''
    for sign in type_zd:
        path_sign = reverse('horoscope-name', args=(sign.__name__,))
        li_elements += f'<li><a href={path_sign}>{sign.__name__}</a></li>'
    if not ul:
        response = f'<ol>{li_elements}</ol>'
    else:
        response = f'<ul>{li_elements}</ul>'
    return HttpResponse(response)


def get_zodiac_by_number(request, zodiac):
    name_zodiac = zodiac_dict[zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac.__name__,))
    return HttpResponseRedirect(redirect_url)


def get_zodiac_by_name(request, zodiac):
    response = f'<h1>{zodiac.title()}</h1><p>{eval(zodiac.title())().description()}</p>'
    return HttpResponse(response)


def get_types(request):
    li_elements = ''
    for att in ('fire', 'earth', 'air', 'water'):
        att = att.title()
        path_sign = reverse('att-name', args=(att, ))
        li_elements += f'<li><a href={path_sign}>{att}</a></li>'
        response = f"""<ul>
                        {li_elements}
                        </ul>
        """
    return HttpResponse(response)


def get_types_att(request, att):
    att = att.lower()
    return index(request, eval(att), ul=True)


def get_zodiac_date(request, day, month):
    for j in zodiac_dict:
        if j.start[1] == month:
            if j.start[0] < day:
                redir = reverse('horoscope-name', args=(j.__name__ ,))
                return HttpResponseRedirect(redir)
            else:
                redir = reverse('horoscope-name', args=(zodiac_dict[zodiac_dict.index(j)-1].__name__ ,))
                return HttpResponseRedirect(redir)