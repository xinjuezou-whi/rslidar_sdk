# Copyright 2025 WheelHub Intelligent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    # Declare launch arguments
    start_rviz_arg = DeclareLaunchArgument('start_rviz', default_value='true')

    rviz_config=get_package_share_directory('rslidar_sdk')+'/rviz/rviz2.rviz'

    config_file = '' # your config file path
    
    return LaunchDescription([
        start_rviz_arg,
        Node(namespace='rslidar_sdk', package='rslidar_sdk', executable='rslidar_sdk_node', output='screen', parameters=[{'config_path': config_file}]),
        Node(namespace='rviz2', package='rviz2', executable='rviz2', arguments=['-d',rviz_config], condition=IfCondition(LaunchConfiguration('start_rviz')))
    ])
