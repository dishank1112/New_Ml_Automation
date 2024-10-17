from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_req(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Ensure no extra whitespace

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='AutomatedModelTraining',  # Avoid double underscores or unusual characters
    version='0.0.1',
    author='Dishank Jain',
    author_email='jainbharti9382@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')
)
