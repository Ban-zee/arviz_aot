import setuptools
from distutils.core import setup
from arviz_aot.aot import module as cc


setuptools.setup(
    name="aot_arviz",
    version="0.0.1",
    author="Ban-zee",
    author_email="aniruddha8@gmail.com",
    description="A small example package",
    packages=['arviz_aot'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=[cc.distutils_extension()],
)
