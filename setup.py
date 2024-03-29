from distutils.core import setup

setup(
    name='django-auditlog',
    version='0.4.4',
    packages=['auditlog', 'auditlog.migrations', 'auditlog.management', 'auditlog.management.commands'],
    package_dir={'': 'src'},
    url='https://github.com/jjkester/django-auditlog',
    license='MIT',
    author='Jan-Jelle Kester',
    description='Audit log app for Django',
    install_requires=[
        'Django>=1.8',
        'jsonfield>=1.0.3',
    ],
    zip_safe=False
)
