#!/usr/bin/env python

import unittest

import rostest

from capabilities.srv import GetCapabilitySpecs


class TestDemo(unittest.TestCase):
    def test_demo(self):
        service_name = '/capability_server/get_capability_specs'
        rospy.wait_for_service(service_name)
        get_capability_specs = rospy.ServiceProxy(service_name, GetCapabilitySpecs)
        response = get_capability_specs()
        assert 'minimal_pkg' in [x.package for x in response.capability_specs], "Invalid capability specs"

if __name__ == '__main__':
    import rospy
    rospy.init_node('demo', anonymous=True)
    rostest.rosrun('capabilities', 'test_demo', TestDemo)
