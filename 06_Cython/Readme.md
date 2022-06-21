# Buildando partes de um programa Cython
- Com o Cython é possivel buildar partes especificas do projeto em C, para ter melhor performance, ou caso tiver preferencia por C.
- Para realizar o build é necessário 2 arquivos o "setup.py" que vai conter instruções de o que deve ser compilado e o ou os arquivos(Pode ser passado mais de 1) ".pyx" que serão compilados para C, note que as importações dos outros arquivos ".py" que usam o módulo, continuam funcionando, pois está sendo refenciado o arquivo ".c" que foi gerado, nem sendo necessário levar os ".pyx" para o local que vai rodar, somente o ".so" é usado na execução pós build.
- Comando para rodar o build:
    - python setup.py build_ext --inplace