# Aqui vai as infos dos módulos cython que querro compilar neste projeto
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["computa.pyx"])
)
