from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='calendario_util',
    version='0.0.1',
    license='MIT License',
    author='Kauê Mandarino',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='kauemandarino@gmail.com',
    keywords='Dias uteis',
    description=u'Mapeador de dias uteis',
    packages=['panda_video'],
    install_requires=['requests'],)