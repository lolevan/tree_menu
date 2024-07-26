from django.db import migrations, models


def create_initial_data(apps, schema_editor):
    Menu = apps.get_model('menu', 'Menu')
    MenuItem = apps.get_model('menu', 'MenuItem')

    # Создаем основное меню
    main_menu = Menu.objects.create(name='main_menu')

    # Создаем элементы меню
    home = MenuItem.objects.create(menu=main_menu, name='Home', url='/home', named_url='home', order=1)
    about = MenuItem.objects.create(menu=main_menu, name='About', url='/about', named_url='about', order=2)
    services = MenuItem.objects.create(menu=main_menu, name='Services', url='/services', named_url='services', order=3)

    # Создаем подэлементы для Services
    web_development = MenuItem.objects.create(menu=main_menu, name='Web Development', url='/services/web-development', named_url='web_development', order=1, parent=services)
    seo = MenuItem.objects.create(menu=main_menu, name='SEO', url='/services/seo', named_url='seo', order=2, parent=services)


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
