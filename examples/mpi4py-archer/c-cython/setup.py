from distutils.core import setup
from Cython.Build import cythonize

setup (
    name = "Fake",
    ext_modules = cythonize('wrapper.pyx'),
)
