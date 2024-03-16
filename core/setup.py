from setuptools import setup
import os 

def get_current_dir():
    return os.path.dirname(os.path.realpath(__file__))

def resolve_paths(*paths):
    return os.path.join(*paths)

readme_path = resolve_paths(get_current_dir(), 'README.md')

setup(
    name = 'composio',
    version = '0.0.1',
    author = 'Utkarsh',
    author_email = 'utkarsh@composio.dev',
    description = 'Core package to act as a bridge between composio platform and other services.',
    long_description = open(readme_path).read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/SamparkAI/composio_sdk',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.7',
    include_package_data = True,
    scripts = ['composio'],
)
