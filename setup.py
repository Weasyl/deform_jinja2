import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
except:
    README = ''

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
except ImportError:
    pass

requires = ['deform', 'Jinja2']

setup(
    name='deform_jinja2',
    version='0.5-2',
    description='Jinja2 templates for Deform widgets',
    long_description=README,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        ],
    keywords='web forms form generation schema validation',
    author="John Anderson",
    author_email="sontek@gmail.com",
    url="https://github.com/sontek/deform_jinja2",
    license="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require = ['pyramid', 'nose'],
    test_suite = "nose.collector"
    )
