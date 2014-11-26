from setuptools import setup, find_packages

version = '0.1'

setup(
    name='jetpack_python',
    version=version,
    description="Game to Improve Python Programming",
    long_description="""\

Game to Improve Python Programming by using librairy Cocos2d

""",
    classifiers=[],
    keywords='cocos',
    author='Alexandre Brun Beraud',
    author_email='abrunberaud@gmail.com',
    url='',
    license='Daniel Moisset, Ricardo Quesada, Rayentray Tappa, Lucio Torre',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        'python2.7',
        'cocos2d',
    ],
    entry_points='__main__',
)