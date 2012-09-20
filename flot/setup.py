from os.path import join, dirname
from distutils.core import setup

try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-flot',
    version='1.3.3',
    url="https://github.com/graingert/django-static-libs/tree/master/flot",
    description='Flot packaged in a handy django app to speed up new applications and reduce duplicaiton.',
    long_description=long_description,
    author='Thomas Grainger',
    author_email='tagrain@gmail.com',
    keywords='django flot js staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['flot'],
    package_data={'flot': [
        'static/lib/flot/jquery.flot*.js',
    ]},
)
