from os.path import join, dirname
from distutils.core import setup

try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-angularjs',
    version='1.0.2',
    url="https://github.com/graingert/django-static-libs/tree/master/angular-1.0.2",
    description='Angularjs packaged in a handy django app to speed up new applications and reduce duplicaiton.',
    long_description=long_description,
    author='Thomas Grainger',
    author_email='tagrain@gmail.com',
    keywords='django angular angularjs staticfiles'.split(),
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
    packages=['angularjs'],
    package_data={'angularjs': [
        'static/lib/angularjs/*.js',
        'static/lib/angularjs/i18n/*.js'
    ]},
)
