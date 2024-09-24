from setuptools import find_packages ,setup
from typing import List

HYPEN_DOT_E = '-e .'
def get_requirments(filepath:str)->List[str]:
    '''
       this function will return list of requirments

    '''
    requirments = []
    with open(filepath) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]

        if HYPEN_DOT_E in requirments:
            requirments.remove(HYPEN_DOT_E)

    return requirments


setup(
        name = 'mlproject',
        version='0.0.1',
        author="Rahul",
        author_email="rahul12mgowda@gmail.com",
        packages=find_packages(),
        install_requires = get_requirments('requirments.txt')
      )