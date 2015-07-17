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


from neutronclient.common import exceptions
from neutronclient.i18n import _
from neutronclient.neutron import v2_0 as neutronv20
from neutronclient.neutron.v2_0.qos import type as qos_rule_types


def add_policy_argument(parser):
    parser.add_argument(
        'policy', metavar='QOS_POLICY',
        help=_('ID or name of the QoS policy.'))


def add_rule_argument(parser):
    parser.add_argument(
        'rule', metavar='QOS_RULE',
        help=_('ID of the QoS rule.'))


def add_type_argument(parser):
    parser.add_argument(
        '--type', choices=qos_rule_types.QOS_RULE_TYPE_LIST,
        help=_('Name of the QoS rule type.'))


def update_policy_args2body(parsed_args, body):
    neutronv20.update_dict(parsed_args, body, ['policy'])


def update_rule_args2body(parsed_args, body):
    neutronv20.update_dict(parsed_args, body, ['rule'])


def update_type_args2body(parsed_args, body):
    neutronv20.update_dict(parsed_args, body, ['type'])


class ListQoSRule(neutronv20.ListCommand):
    """List all qos rules belonging to the specified policy."""
    resource = 'policy'

    list_columns = ['id']
    _formatters = {}
    pagination_support = True
    sorting_support = True

    def add_known_arguments(self, parser):
        add_policy_argument(parser)

    def args2body(self, parsed_args):
        body = {}
        update_policy_args2body(parsed_args, body)
        return {self.resource: body}

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        _policy_id = (
            neutronv20.find_resourceid_by_name_or_id(neutron_client,
                                                     self.resource,
                                                     parsed_args.policy))
        neutron_client.list_qos_rules(_policy_id)


class ShowQoSRule(neutronv20.ShowCommand):
    """Show information about the given qos rule."""

    resource = 'policy'

    def add_known_arguments(self, parser):
        add_rule_argument(parser)

    def args2body(self, parsed_args):
        body = {}
        update_rule_args2body(parsed_args, body)
        return {'qos_rule': body}

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        self.args2body(parsed_args)
        _policy_id = neutronv20.find_resourceid_by_name_or_id(neutron_client,
                                                              self.resource,
                                                              parsed_args.id)
        neutron_client.show_qos_rule(_policy_id, parsed_args.rule)


class CreateQoSRule(neutronv20.CreateCommand):
    """Create a qos rule."""

    resource = 'policy'

    def add_known_arguments(self, parser):
        add_policy_argument(parser)
        add_type_argument(parser)
        qos_rule_types.add_type_param_arguments(parser)

    def args2body(self, parsed_args):
        body = {}
        if not parsed_args.type:
            raise exceptions.CommandError(_("Must provide type option."))
        qos_rule_types.update_type_param_args2body(parsed_args, body)
        return {(parsed_args.type + '_rule'): body}

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        body = self.args2body(parsed_args)
        _policy_id = (
            neutronv20.find_resourceid_by_name_or_id(neutron_client,
                                                     self.resource,
                                                     parsed_args.policy))
        qos_rule_types.call_create_api(neutron_client, _policy_id,
                                       parsed_args.type, body)


class UpdateQoSRule(neutronv20.UpdateCommand):
    """Update the given qos rule."""
    resource = 'policy'

    def add_known_arguments(self, parser):
        add_rule_argument(parser)
        add_type_argument(parser)
        qos_rule_types.add_type_param_arguments(parser)

    def args2body(self, parsed_args):
        body = {}
        if not parsed_args.type:
            raise exceptions.CommandError(_("Must provide type option."))
        update_rule_args2body(parsed_args, body)
        qos_rule_types.update_type_param_args2body(parsed_args, body)
        return {(parsed_args.type + '_rule'): body}

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        body = self.args2body(parsed_args)
        _policy_id = neutronv20.find_resourceid_by_name_or_id(neutron_client,
                                                              self.resource,
                                                              parsed_args.id)
        qos_rule_types.call_update_api(neutron_client, _policy_id,
                                       parsed_args.rule, parsed_args.type,
                                       body)


class DeleteQoSRule(neutronv20.DeleteCommand):
    """Delete the given qos rule."""
    resource = 'policy'

    def add_known_arguments(self, parser):
        add_rule_argument(parser)

    def args2body(self, parsed_args):
        body = {}
        update_rule_args2body(parsed_args, body)
        return {'qos_rule': body}

    def run(self, parsed_args):
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        self.args2body(parsed_args)
        _policy_id = neutronv20.find_resourceid_by_name_or_id(neutron_client,
                                                              self.resource,
                                                              parsed_args.id)
        neutron_client.delete_qos_rule(_policy_id, parsed_args.rule)
