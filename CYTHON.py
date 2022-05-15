import os
from setuptools import setup
from Cython.Build import cythonize


os.system('clear')
pahrul = input ('(+) enter your file : ')
setup(
    ext_modules = cythonize(""+ pahrul + "")
)

print('(+) Finished...')