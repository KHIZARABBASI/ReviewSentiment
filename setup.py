from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requiremets(file_path : str) -> List[str]:
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement= [req.replace("\n", "") for req in requirement]

        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)
    return requirement 



setup(
    name= "Review Sentiments",
    version= "0.0.1",
    description= " xyz",
    author= "Khizar Abbasi",
    author_email="Khizerabbasi144@gmail.com",
    packages= find_packages(),
    install_requires= get_requiremets("requirements.txt")
)