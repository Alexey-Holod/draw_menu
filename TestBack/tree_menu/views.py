from django.shortcuts import render


# Create your views here.
def menu(request, what_menu='', planet=''):
    if what_menu == '' and planet == '':
        return render(request, 'tree_menu/base.html')
    else:
        context = {'artilcle': 'Раздел: ' + what_menu + '</br>' + ' Статья про ' + planet}
        return render(request, 'article/article.html', context)
