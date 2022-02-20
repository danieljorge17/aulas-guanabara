# Exercício 21

import os

diretorio_absoluto = os.path.dirname(os.path.realpath(__file__))
diretorio_da_musica = os.path.join(diretorio_absoluto, 'musicas/Chitãozinho & Xororó - Evidências.mp3')

os.system('afplay "{}"'.format(diretorio_da_musica))
