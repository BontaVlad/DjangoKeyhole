from setuptools import setup, find_packages


setup(
    name="DjangoKeyhole",
    version="0.1dev",
    author="Bonta Sergiu Vlad",
    author_email="bonta.vlad@gmail.com",
    packages=find_packages(),
    package_data={
        'static/crop_widget/js': ['*.js'],
        'static/crop_widget/css': ['*.css', '*.png'],
    },
    include_package_data=True,
    license="MIT License, see LICENSE.txt",
    description="Django form widget for croping uploaded images based on "
                "a predefined size",
    long_description=open('README.txt').read()
)
