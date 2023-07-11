from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A python library for ensuring the safety and security of visual content'
LONG_DESCRIPTION = 'A Python package to set restrictions on visual content of all kinds and protect users from seeing harmful content, and ensure the safety of input and output machine learning models.'

# Setting up
setup(
    name="zein",
    version=VERSION,
    author="Mohamed Elsayed",
    author_email="<mohamedelsayed3487@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    package_data= {
      'zein': ['models/*.pkl', 'data/*.csv', 'retrained_labels.txt'],
    },

    zip_safe=False,
    install_requires=['pandas', 'joblib', 'tensorflow', 'scikit-learn>=0.24.2'],
    keywords=['python','arabic filtering', 'text filtering', 'profanity check'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
    
)




