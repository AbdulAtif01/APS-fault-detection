from setuptools import find_packages,setup

from typing import List

REQUIRMENT_FILE_NAME = "requirements.txt"

def get_requirements()-> list(str):
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    

setup(
    name="sensor",
    version="0.0.2",
    author="Abdul",
    author_email="abdulimrann1@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)