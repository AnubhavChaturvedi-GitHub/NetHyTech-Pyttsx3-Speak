import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NetHyTech-Pyttsx3-Speak",
    version="1.0",
    author="Anubhav Chaturvedi",
    author_email="chaturvedianubhav520@gmail.com",
    description="A package for controlling mouse actions using hand gestures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnubhavChaturvedi-GitHub/NetHyTech-MCV",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyttsx3',
        'textblob'
    ]
)


'''
python setup.py bdist_wheel 

twine upload --repository-url https://upload.pypi.org/legacy/ dist/*  
'''