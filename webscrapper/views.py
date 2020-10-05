import requests
import re

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from lxml import html

from webscrapper.business_object.review import Review


def extract_note(note_phrase):
    """
    Prend une note sous forme XX sur YY étoiles et retourne un dictionnaire
    {"note" : XX, "note_max" : YY}
    :param note_phrase: la phrase à parser
    :type note_phrase: str
    :return: un dictonnaire avec la note et la note max
    :rtype: dict
    """
    notes = re.findall(r"[-+]?\d*\.\d+|\d+", note_phrase.replace(",", "."))

    return {"note" : notes[0], "note_max" : notes[1]}

def reviews_product(request):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    headers = {'User-Agent': user_agent}

    url = request.POST['url_scrap']

    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    print(tree)
    internautes = tree.xpath("//span[@class='a-profile-name']/text()")
    titres = tree.xpath("//*[contains(@class, "
                        "'review-title-content')]/span/text()")
    notes = tree.xpath("//i[contains(@class, 'review-rating')]/span/text()")
    avis = tree.xpath("//div[contains(@class, "
                      "'review-text-content')]")


    reviews =[]
    for i in range(len(titres)):
        dict_note = extract_note(notes[i])
        review = Review(auteur=internautes[i],
                        titre=titres[i],
                        contenu=avis[i][0].text,
                        note=dict_note["note"],
                        note_max=dict_note["note_max"]
                        )

        reviews.append(review)

    template = loader.get_template('webscrapper/reviews_product.html')
    context = {
        'reviews': reviews,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('webscrapper/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))