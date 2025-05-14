'''
sera criada um arquivo __pycache__
funciona da seguinte maneira, quando você executa um script em Python, o interpretador o compila para versão bytecode pyc e após isso guarda no diretório __pycache__.
Boa prática
Quando você for compartilhar o seu código com outras pessoas, a prática comum é deletar esse diretório. 
Caso, você suba o seu código através de um controle de versão git, é necessário listar o __pycache__ no arquivo .gitignore, 
para que a pasta não seja incluída no git push


Para ignorar este arquivo , podera criar um arquivo no mesmo diretorio com nome ----> .gitignore ---
detro do arquivo os seguintes comandos:
__pycache__
.gitignore

ou se for fora do diretorio o seguinte comando
exemplo : funcoes05/__pycache__
'''