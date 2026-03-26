from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'osl_motor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hari-prasad-gajurel',
    maintainer_email='hari-prasad-gajurel@todo.todo',
    description='Motor simulation for OSLSim in ROS2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_sim = osl_motor.motor_sim:main'
        ],
    },
)
