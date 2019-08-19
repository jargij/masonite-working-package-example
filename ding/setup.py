from setuptools import setup

setup(
    name="ding",
    version='0.0.1',
    packages=[
        'ding',
        'ding.commands',
        'ding.contracts',
        'ding.drivers',
        'ding.managers'
    ],
    install_requires=[
        'masonite',
    ],
    include_package_data=True,
)
