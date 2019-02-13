"""
    A simple way to get data out of a remote machine using SNMP without having to deal with a single MIB or OID

    The goal of Ecks3 is simple - make it really easy to get get any data
    from an SNMP service.

    Ecks3 is made up of a core class that will collect data via SNMP,
    and a set of plugins that contain the OID and the code needed to
    transform the results from nested OID's to usable data.

    See help(ecks3.Ecks) for more info


    Copyright 2011-2015 Chris Read (chris.read@gmail.com)
    Copyright 2019 Alexander Fefelov <alexanderfefelov@yandex.ru>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from .ecks3 import Ecks
