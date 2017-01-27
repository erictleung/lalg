from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='lalg',
      version='0.0.1',
      description='Python library to experiment with Linear Algebra concepts',
      long_description=readme(),
      url='https://github.com/erictleung/lalg',
      author='Eric Leung',
      author_email='eric@erictleung.com ',
      license='MIT',
      packages=['lalg'],
      install_requires=[
          'numpy'
      ],
      zip_safe=False)
