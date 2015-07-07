# Copyright 2015 Huawei Technologies India Pvt Ltd.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import sys


from neutronclient.neutron.v2_0.qos import policy as qos_policy
from neutronclient.tests.unit import test_cli20


class CLITestV20QoSPolicyJSON(test_cli20.CLITestV20Base):
    def setUp(self):
        super(CLITestV20QoSPolicyJSON, self).setUp()

    def test_create_qos_policy_with_only_keyattributes(self):
        """Create qos policy: abc."""
        resource = 'qos_policy'
        cmd = qos_policy.CreateQoSPolicy(test_cli20.MyApp(sys.stdout),
                                         None)
        myid = 'myid'
        name = 'abc'
        args = [name]
        position_names = ['name']
        position_values = [name]
        self._test_create_resource(resource, cmd, name, myid, args,
                                   position_names, position_values)

    def test_create_qos_policy_with_description(self):
        """Create qos policy: abc."""
        resource = 'qos_policy'
        cmd = qos_policy.CreateQoSPolicy(test_cli20.MyApp(sys.stdout),
                                         None)
        myid = 'myid'
        name = 'abc'
        description = 'policy_abc'
        args = [name, '--description', description]
        position_names = ['name', 'description']
        position_values = [name, description]
        self._test_create_resource(resource, cmd, name, myid, args,
                                   position_names, position_values)

    def test_create_qos_policy_with_shared(self):
        """Create qos policy: abc shared across tenants"""
        resource = 'qos_policy'
        cmd = qos_policy.CreateQoSPolicy(test_cli20.MyApp(sys.stdout),
                                         None)
        myid = 'myid'
        name = 'abc'
        description = 'policy_abc'
        args = [name, '--description', description, '--shared']
        position_names = ['name', 'description', 'shared']
        position_values = [name, description, True]
        self._test_create_resource(resource, cmd, name, myid, args,
                                   position_names, position_values)

    def test_create_qos_policy_with_unicode(self):
        """Create qos policy: u'\u7f51\u7edc'."""
        resource = 'qos_policy'
        cmd = qos_policy.CreateQoSPolicy(test_cli20.MyApp(sys.stdout),
                                         None)
        myid = 'myid'
        name = u'\u7f51\u7edc'
        description = u'\u7f51\u7edc'
        args = [name, '--description', description]
        position_names = ['name', 'description']
        position_values = [name, description]
        self._test_create_resource(resource, cmd, name, myid, args,
                                   position_names, position_values)

    def test_update_qos_policy(self):
        """qos_policy-update myid --name newname."""
        resource = 'qos_policy'
        cmd = qos_policy.UpdateQoSPolicy(test_cli20.MyApp(sys.stdout),
                                         None)
        self._test_update_resource(resource, cmd, 'myid',
                                   ['myid', '--name', 'newname'],
                                   {'name': 'newname', })

    def test_update_qos_policy_description(self):
        """qos_policy-update myid --name newname. --description newdesc"""
        resource = 'qos_policy'
        cmd = qos_policy.UpdateQoSPolicy(test_cli20.MyApp(sys.stdout),
                                         None)
        self._test_update_resource(resource, cmd, 'myid',
                                   ['myid', '--description', 'newdesc'],
                                   {'description': 'newdesc', })

    def test_list_qos_policies(self):
        """qos-policy-list."""
        resources = "qos_policies"
        cmd = qos_policy.ListQoSPolicy(test_cli20.MyApp(sys.stdout),
                                       None)
        self._test_list_resources(resources, cmd, True)

    def test_list_qos_policies_pagination(self):
        """qos-policy-list."""
        resources = "qos_policies"
        cmd = qos_policy.ListQoSPolicy(test_cli20.MyApp(sys.stdout),
                                       None)
        self._test_list_resources_with_pagination(resources, cmd)

    def test_list_qos_policies_sort(self):
        """sorted list: qos-policy-list --sort-key name --sort-key id
        --sort-key asc --sort-key desc
        """
        resources = "qos_policies"
        cmd = qos_policy.ListQoSPolicy(test_cli20.MyApp(sys.stdout),
                                       None)
        self._test_list_resources(resources, cmd,
                                  sort_key=["name", "id"],
                                  sort_dir=["asc", "desc"])

    def test_list_qos_policies_limit(self):
        """size (1000) limited list: qos-policy-list -P."""
        resources = "qos_policies"
        cmd = qos_policy.ListQoSPolicy(test_cli20.MyApp(sys.stdout),
                                       None)
        self._test_list_resources(resources, cmd, page_size=1000)

    def test_show_qos_policy_id(self):
        """qos-policy-show test_id."""
        resource = 'qos_policy'
        cmd = qos_policy.ShowQoSPolicy(test_cli20.MyApp(sys.stdout),
                                       None)
        args = ['--fields', 'id', self.test_id]
        self._test_show_resource(resource, cmd, self.test_id, args, ['id'])

    def test_show_qos_policy_id_name(self):
        """qos-policy-show."""
        resource = 'qos_policy'
        cmd = qos_policy.ShowQoSPolicy(test_cli20.MyApp(sys.stdout),
                                       None)
        args = ['--fields', 'id', '--fields', 'name', self.test_id]
        self._test_show_resource(resource, cmd, self.test_id,
                                 args, ['id', 'name'])

    def test_delete_qos_policy(self):
        """qos-policy-delete my-id."""
        resource = 'qos_policy'
        cmd = qos_policy.DeleteQoSPolicy(test_cli20.MyApp(sys.stdout),
                                         None)
        my_id = 'myid1'
        args = [my_id]
        self._test_delete_resource(resource, cmd, my_id, args)
