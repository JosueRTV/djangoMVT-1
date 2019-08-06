from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
# Create your views here.

posts = [
    {
        'name':'Como la flor',
        'user': 'Josue Torres',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://image.freepik.com/foto-gratis/imagen-primer-plano-flores-imagen-macro-utiliza-como-imagen-fondo-foto-primer-plano-macro_34433-346.jpg',
    },
    {
        'name':'Luna',
        'user': 'Ruben Torres',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://dam.ngenespanol.com/wp-content/uploads/2019/03/luna-colores-nuevo-770x395.png',
    },
    {
        'name':'Luna',
        'user': 'Silvia Valdez',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://d500.epimg.net/cincodias/imagenes/2018/11/13/lifestyle/1542113135_776401_1542116070_noticia_normal.jpg',
    },
]

    # .format(**post))
    # import pdb; pdb.set_trace()

def list_posts(request):
    # """Busca automaticamente dentro de la carpeta tempplates
    # y recive como argumento contexto que es un diccionario """
    return render(request, 'feed.html', { 'posts': posts }) 

    # content = []
    # for post in posts:
    #     content.append("""
    #         <p><strong>{name}</strong></p>
    #         <p><small>{user} - <i>{timestamp}</i></small></p>
    #         <figure><img src="{picture}"></figure>
    #     """.format(name=post['name'], user=post['user'], picture=post['picture'], timestamp=post['timestamp']))
    # return HttpResponse('<br>'.join(content))