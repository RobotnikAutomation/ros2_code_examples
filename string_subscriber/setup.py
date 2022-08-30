# Lines added after creation of the launch
import os
from glob import glob
# END - Lines added after creation of the launch
from setuptools import setup

package_name = 'string_subscriber'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Line added after creation of the launch
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robot',
    maintainer_email='smoreno@robotnik.es',
    description='Example of ROS2 subscription to a ROS1 topic',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Line added after creation of the sub code
            'string_listener = string_subscriber.string_subscriber_function:main',
        ],
    },
)
