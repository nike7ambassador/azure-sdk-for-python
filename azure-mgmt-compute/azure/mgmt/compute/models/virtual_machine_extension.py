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


class VirtualMachineExtension(Resource):
    """
    Describes a Virtual Machine Extension.

    :param str id: Resource Id
    :param str name: Resource name
    :param str type: Resource type
    :param str location: Resource location
    :param dict tags: Resource tags
    :param str publisher: Gets or sets the name of the extension handler
     publisher.
    :param str virtual_machine_extension_type: Gets or sets the type of the
     extension handler.
    :param str type_handler_version: Gets or sets the type version of the
     extension handler.
    :param bool auto_upgrade_minor_version: Gets or sets whether the
     extension handler should be automatically upgraded across minor versions.
    :param str force_update_tag: Gets or sets whether the extension handler
     should be forced to re-run even if the extension configuration has not
     changed.
    :param object settings: Gets or sets Json formatted public settings for
     the extension.
    :param object protected_settings: Gets or sets Json formatted protected
     settings for the extension.
    :param str provisioning_state: Gets or sets the provisioning state, which
     only appears in the response.
    :param VirtualMachineExtensionInstanceView instance_view: Gets or sets
     the virtual machine extension instance view.
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'virtual_machine_extension_type': {'key': 'properties.type', 'type': 'str'},
        'type_handler_version': {'key': 'properties.typeHandlerVersion', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
        'settings': {'key': 'properties.settings', 'type': 'object'},
        'protected_settings': {'key': 'properties.protectedSettings', 'type': 'object'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'instance_view': {'key': 'properties.instanceView', 'type': 'VirtualMachineExtensionInstanceView'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, publisher=None, virtual_machine_extension_type=None, type_handler_version=None, auto_upgrade_minor_version=None, force_update_tag=None, settings=None, protected_settings=None, provisioning_state=None, instance_view=None, **kwargs):
        super(VirtualMachineExtension, self).__init__(id=id, name=name, type=type, location=location, tags=tags, **kwargs)
        self.publisher = publisher
        self.virtual_machine_extension_type = virtual_machine_extension_type
        self.type_handler_version = type_handler_version
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.force_update_tag = force_update_tag
        self.settings = settings
        self.protected_settings = protected_settings
        self.provisioning_state = provisioning_state
        self.instance_view = instance_view
