# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class SlotDifference(Resource):
    """
    An object describing the difference in setting values between two web app
    slots

    :param str id: Resource Id
    :param str name: Resource Name
    :param str location: Resource Location
    :param str type: Resource type
    :param dict tags: Resource tags
    :param str slot_difference_type: Indicates the type of the difference:
     Information, Warning or Error.
    :param str setting_type: The type of the settings: General, AppSetting or
     ConnectionString
    :param str diff_rule: Rule that describes how to process the difference
     in settings during web app slot swap.
    :param str setting_name: Name of the setting
    :param str value_in_current_slot: Value of the setting in the current web
     app slot
    :param str value_in_target_slot: Value of the setting in the target web
     app slot
    :param str description: Description of the difference
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'slot_difference_type': {'key': 'properties.type', 'type': 'str'},
        'setting_type': {'key': 'properties.settingType', 'type': 'str'},
        'diff_rule': {'key': 'properties.diffRule', 'type': 'str'},
        'setting_name': {'key': 'properties.settingName', 'type': 'str'},
        'value_in_current_slot': {'key': 'properties.valueInCurrentSlot', 'type': 'str'},
        'value_in_target_slot': {'key': 'properties.valueInTargetSlot', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, slot_difference_type=None, setting_type=None, diff_rule=None, setting_name=None, value_in_current_slot=None, value_in_target_slot=None, description=None, **kwargs):
        super(SlotDifference, self).__init__(id=id, name=name, location=location, type=type, tags=tags, **kwargs)
        self.slot_difference_type = slot_difference_type
        self.setting_type = setting_type
        self.diff_rule = diff_rule
        self.setting_name = setting_name
        self.value_in_current_slot = value_in_current_slot
        self.value_in_target_slot = value_in_target_slot
        self.description = description
