# Lines added after creation of the launch
import os
from glob import glob
# END - Lines added after creation of the launch
from setuptools import setup

package_name = 'py_pubsub'

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
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Line added after creation of the pub code
            'talker = py_pubsub.publisher_member_function:main',
            # Line added after creation of the sub code
            'listener = py_pubsub.subscriber_member_function:main',
        ],
    },
)
