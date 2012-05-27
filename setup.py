from setuptools import setup, find_packages

pkg_name = 'radpress'
version = __import__(pkg_name).__version__


setup(
    name=pkg_name,
    version=version,
    description='Simple reusable blog application',
    author='Gokmen Gorgen',
    author_email='gokmen@radity.com',
    license='GPLv3',
    packages=find_packages(exclude=['venv', 'demo', 'docs']),
    package_data={pkg_name: ['radpress/templates/radpress/*.html']},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.4',
        'docutils==0.9'
    ]
)
