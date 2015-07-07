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

"""
    Note: Below list and dictionary must be update for
    newer qos rule type supports like DSCP, ECN, VLAN
    tagging and etc in the future.
"""
BANDWIDTH_LIMIT = 'bandwidth_limit'
QOS_RULE_TYPE_LIST = [BANDWIDTH_LIMIT]

"""
    Rule type: bandwidth_limit
    Resource: qos_bandwidth_limit_rule
    For any new rule types support update here as well.
"""
type_resource = {
    BANDWIDTH_LIMIT: 'qos_bandwidth_limit_rule',
}


def add_bandwidth_limit_arguments(parser):
    parser.add_argument(
        '--max_kbps',
        help=_('max bandwidth in kbps.'))
    parser.add_argument(
        '--max_burst_kbps',
        help=_('Max burst bandwidth in kbps.'))


def add_type_param_arguments(parser):
    """Function to add qos rule type arguments."""
    add_bandwidth_limit_arguments(parser)


def update_bandwidth_limit_args2body(parsed_args, body):
    if parsed_args.type != BANDWIDTH_LIMIT:
        return

    m_kbps = parsed_args.max_kbps
    b_kbps = parsed_args.max_burst_kbps
    if (not m_kbps and not b_kbps):
        raise exceptions.CommandError(_("Must provide max_kbps"
                                        " or max_burst_kbps option."))

    neutronv20.update_dict(parsed_args, body,
                           ['max_kbps', 'max_burst_kbps'])


def update_type_param_args2body(parsed_args, body):
    """Function to parse qos rule type arguments."""
    update_bandwidth_limit_args2body(parsed_args, body)


def call_create_api(neutron_client, policy_id, rule_type, body):
    if rule_type in type_resource.keys():
        create_api = getattr(neutron_client,
                             "create_%s" % type_resource[rule_type])
        return create_api(policy_id, body)


def call_update_api(neutron_client, policy_id, rule_id, rule_type, body):
    if rule_type in type_resource.keys():
        update_api = getattr(neutron_client,
                             "update_%s" % type_resource[rule_type])
        return update_api(policy_id, rule_id, body)
