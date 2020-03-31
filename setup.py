from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(  name='LEDController',
        version='0.0.1',
        description='Wrapper for rpi_ws281x including functionality to use an LED matrix',
        long_description=readme(),
        long_description_content_type='text/markdown',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: Raspbian'
        ],
        url='https://github.com/tharrry/LEDController',
        author='tharrry',
        author_mail='martin.leger@outlook.de',
        keywords='raspbian raspberry raspberrypi pi led gpio rpi rpi_ws281x ws281x',
        license='MIT',
        packages=['LEDController'],
        install_requires=['rpi_ws281x'],
        include_package_data=True,
        zip_safe=False
)