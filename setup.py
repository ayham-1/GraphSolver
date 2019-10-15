from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='GraphSolver',
    version='0.0.1',
    description='An application for solving linear\quadratic graphs.',
    long_description=readme,
    author='altf_four',
    author_email='ayhamaboualfadl@gmail.com',
    url='https://github.com/realaltffour/GraphSolver',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
