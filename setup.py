try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='tiny_rsa',
    version='0.0.1',
    url='https://github.com/OpenGroper/tiny_rsa',
    license='MIT License',
    author='Shuge Lee',
    author_email='shuge.lee@gmail.com',
    description='RSA in pure Python',

    packages = [
        "tiny_rsa",
        "tiny_rsa.tests",
    ],
    test_suite ="tiny_rsa.tests",
)
