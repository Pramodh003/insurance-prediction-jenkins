from setuptools import find_packages , setup
from typing import List

HYPHON_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        
        if HYPHON_DOT in requirements:
            requirements.remove(HYPHON_DOT)
    return requirements

setup(
    name = "Medical Insurance end to end to pipeline",
    version="0.0.1",
    author="Pramodh B R",
    author_email="pramodhbr29@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)