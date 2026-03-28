from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_jazzy'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'data'), [f for f in glob('data/*') if os.path.isfile(f)]),
        (os.path.join('share', package_name, 'launch'), [f for f in glob('launch/*') if os.path.isfile(f)]),
        (os.path.join('share', package_name, 'urdf'), [f for f in glob('urdf/*') if os.path.isfile(f)]),
        (os.path.join('share', package_name, 'config'), [f for f in glob('config/*') if os.path.isfile(f)]),
        (os.path.join('share', package_name, 'meshes'), [f for f in glob('meshes/*') if os.path.isfile(f)]),
        (os.path.join('share', package_name, 'worlds'), [f for f in glob('worlds/*') if os.path.isfile(f)]),
    ],
    install_requires=['setuptools', 'numpy', 'pyyaml'],
    zip_safe=True,
    maintainer='pika',
    maintainer_email='pika@todo.todo',
    description='TODO: Package description',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'oslsim_controller = ros2_jazzy.controller:main',
            'loadcell = ros2_jazzy.loadcell:main',
            'oslsim_walker = ros2_jazzy.walk:main',
            'oslsim_pid_tuner = ros2_jazzy.tuner:main',
        ],
    },
)
