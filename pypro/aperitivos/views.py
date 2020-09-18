from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, title, id):
        self.slug = slug
        self.title = title
        self.id = id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos_list = [
    Video('motivacao', 'Video Aperitivo: Motivação', 'aaK-H1EHmA4'),
    Video('instalacao-windows', 'Video Aperitivo: Instalação do Windows', 'SmpSOxkiYBA')
]

videos_dct = {v.slug: v for v in videos_list}


def indice(request):
    return render(request, "aperitivos/indice.html", context={"videos": videos_list})


def video(request, slug):
    video_dct = videos_dct[slug]
    return render(request, "aperitivos/video.html", context={"video": video_dct})
