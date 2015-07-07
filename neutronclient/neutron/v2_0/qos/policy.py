# Copyright 2015 Huawei Technologies India Pvt Ltd, Inc.
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

from neutronclient.i18n import _
from neutronclient.neutron import v2_0 as neutronv20


class ListQoSPolicy(neutronv20.ListCommand):
    """List QoS policies that belong to a given tenant connection."""

    resource = 'policy'
    list_columns = ['id', 'name']
    _formatters = {}
    pagination_support = True
    sorting_support = True


class ShowQoSPolicy(neutronv20.ShowCommand):
    """Show information of a given qos policy."""

    resource = 'policy'


class CreateQoSPolicy(neutronv20.CreateCommand):
    """Create a qos policy."""

    resource = 'policy'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of QoS policy to create.'))
        parser.add_argument(
            '--description',
            help=_('Description of the QoS policy.'))
        parser.add_argument(
            '--shared',
            action='store_true',
            help=_('Accessible by other tenants. '
                   'Set shared to True (default is False).'))

    def args2body(self, parsed_args):
        body = {self.resource: {'name': parsed_args.name}, }
        if parsed_args.description:
            body[self.resource].update(
                {'description': parsed_args.description})
        if parsed_args.shared:
            body[self.resource].update(
                {'shared': parsed_args.shared})
        return body


class UpdateQoSPolicy(neutronv20.UpdateCommand):
    """Update a given qos policy."""

    resource = 'policy'

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--description',
            help=_('Description of the QoS policy.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }
        if parsed_args.description:
            body[self.resource].update(
                {'description': parsed_args.description})
        return body


class DeleteQoSPolicy(neutronv20.DeleteCommand):
    """Delete a given qos policy."""

    resource = 'policy'
