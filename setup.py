from setuptools import find_packages,setup

HYPEN_E_DOT = "-e ."


def get_requirements(file_path):

    requirements = []
    #read requirements.txt
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        # remove newline
        requirements = [ req.replace("\n","") for req in requirements]
        # remove HYPEN_E_DOT
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements





setup(
    name = "insurence_prediction",
    version="0.0.1",
    author="ravi",
    author_email="81ravikiran@gmail.com",
    packages=find_packages(),
    install_requires  =  get_requirements("requirements.txt")
)