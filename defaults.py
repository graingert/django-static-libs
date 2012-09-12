DEFAULTS = dict(
    name='django-{lib}',
    url="https://github.com/graingert/django-static-libs/tree/master/{lib}",
    description='{lib} packaged in a handy django app to speed up new applications and reduce duplicaiton.',
    long_description=long_description,
    author='Thomas Grainger',
    author_email='tagrain@gmail.com',
    keywords='django {lib} {keywords} staticfiles'.split(),
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
    packages=['{lib}'],
    package_data={'{lib}': [
        'static/lib/{lib}/js/*.js'
    ]},
)
