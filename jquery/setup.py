from os.path import join, dirname
from distutils.core import setup

try:
    f = open(join(dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-jquery',
    version='1.8.0',
    url="http://bitbucket.org/massimilianoravelli/django-jquery",
    description='jQuery packaged in an handy django app to speed up new applications and deployment.',
    long_description=long_description,
    author='Massimiliano Ravelli',
    author_email='massimiliano.ravelli@gmail.com',
    license='MIT',
    keywords='django jquery staticfiles'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['jquery'],
    package_data={'jquery': ['static/js/*.js']},
)
