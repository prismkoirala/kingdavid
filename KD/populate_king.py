import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','KD.settings')

import django
django.setup()


##fake popscript

import random
from king.models import ProductID, ProductPage
from faker import Faker

fakegen = Faker()
topics = ['Shampoo', 'Beard Oil', 'Perfume', 'Bodyspray', 'Lotion']


def add_topic():
    t = ProductID.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_text = fakegen.company()
        fake_name = fakegen.company()
        fake_name2 = fakegen.company()
        fake_date = fakegen.date()
        fake_date2 = fakegen.date()
        m_page = ProductID.objects.get_or_create(date=fake_date2)
        p_page = ProductPage.objects.get_or_create(p_id=top,p_title=fake_name,p_desc=fake_text)[0]

if __name__ == '__main__':
    print("populating scripts!")
    populate(10)
    print('populating complete!')
