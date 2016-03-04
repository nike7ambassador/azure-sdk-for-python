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

from msrest.serialization import Model


class CheckAvailabilityResource(Model):
    """
    Description of a CheckAvailibility resource.

    :param str id: Gets or sets the id
    :param str location: Gets or sets datacenter location
    :param str name: Gets or sets name
    :param str type: Gets or sets resource type
    :param dict tags: Gets or sets tags
    :param bool is_availiable: Gets or sets true if the name is available and
     can be used to create new Namespace/NotificationHub. Otherwise false.
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'is_availiable': {'key': 'isAvailiable', 'type': 'bool'},
    }

    def __init__(self, id=None, location=None, name=None, type=None, tags=None, is_availiable=None, **kwargs):
        self.id = id
        self.location = location
        self.name = name
        self.type = type
        self.tags = tags
        self.is_availiable = is_availiable
