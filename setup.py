from setuptools import setup, find_packages

version = '0.1'

setup(
    name='pyjetpack',
    version=version,
    description="Game to Improve Python Programming",
    long_description="""\

Game to Improve Python Programming by using librairy Cocos2d

""",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
    ],
    keywords='cocos',
    author='Alexandre Brun Beraud',
    author_email='abrunberaud@gmail.com',
    url='',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'cocos2d',
    ],
    entry_points=dict(
        console_scripts=[
            'pyjetpack = pyjetpack.cli:main',
        ],
    ),
)
