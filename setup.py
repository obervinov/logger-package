from setuptools import setup

setup(
    name = 'logger', 
    version = '1.0.0',
    description = 'This is a custom log formatter package from python projects.',
    py_modules = ["logger"],
    package_dir = {'':'src'},
    author = 'Oleg Bervinov',
    author_email = 'unknown-312@ya.ru',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/obervinov/logger-package',
    include_package_data=True,
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Text Processing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    keywords = ['Logs'],
    
)