from setuptools import find_packages,setup


HYPEN_E_DOT='-e .'

# function to get the libraries from requirements.txt
def get_requirements(file_path):
    requirements = []
    with open(file_path) as fp:
        requirements = fp.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(

    name = "British_Airways_Virtual_Project",
    version = "0.0.1",
    author = "surya sai",
    author_email = "suryakadali1994@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('/Users/suryasaikadali/Downloads/Virtual_Projects/VP_British_Airways/requirements.txt')

)
