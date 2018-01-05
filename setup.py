from setuptools import setup, find_packages

setup(
    name = 'cramerfish',
    version = '0.0.1',
    keywords = ('crypto', 'md5', 'threefish', 'cramershoup'),
    description = 'The Implementation Of ThreeFish And CramerShoup In Python3',
    license = 'MIT License',
    install_requires = [
        'colorama== 0.3.9',
        'keyboard== 0.11.0',
    ],
    author = 'GopherJ',
    author_email = 'cocathecafe@gmail.com',
    packages = find_packages(exclude=['image']),
    package_data = {
       '' : ['script/*'], 
    },
    platforms = 'any',
    url = 'https://github.com/GopherJ/ThreeFishAndCramerShoup',
    scripts = ['cmd.py'],
)
