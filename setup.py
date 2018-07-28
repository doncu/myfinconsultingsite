import glob
import pathlib
import collections


import setuptools
from pip._internal import req


def get_recursive_files(src, dst):
    data_files = collections.defaultdict(list)
    for path in glob.glob('{}/**/*'.format(src), recursive=True):
        path_obj = pathlib.Path(path)
        if path_obj.is_file():
            new_path = (dst, ) + path_obj.parent.parts[1:]
            dirname = pathlib.Path(*new_path)
            data_files[str(dirname)].append(path)

    return tuple(data_files.items())


setuptools.setup(
    name='myfinconsulting',
    version='0.0.1',
    author='Semen Dontsu, Ivan Krivosheev',
    author_email='doncusemen@gmail.com, py.krivosheev@gmail.com',
    description='Site for myfinconsulting',
    url='http://myfinconsulting.ru/',
    zip_safe=False,
    python_requires='>=3.5',
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'myfinconsulting=myfinconsulting.cli:cli',
        ]
    },
    data_files=get_recursive_files('etc', 'etc') + get_recursive_files('static', 'static') + get_recursive_files('images', 'images'),
    install_requires=[str(ir.req) for ir in req.parse_requirements('requirements.txt', session='hack')]
)
