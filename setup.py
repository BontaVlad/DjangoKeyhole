from setuptools import setup, find_packages


setup(
    name="DjangoKeyhole",
    version="0.5.dev0",
    author="Bonta Sergiu Vlad",
    author_email="bonta.vlad@gmail.com",
    url="https://github.com/BontaVlad/DjangoKeyhole",
    packages=find_packages(),
    package_data={
        'static/crop_widget/js': ['*.js'],
        'static/crop_widget/css': ['*.css', '*.png'],
    },
    include_package_data=True,
    license="MIT License, see LICENSE.txt",
    description="Django form widget for cropping uploaded images based on "
                "a predefined size",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
