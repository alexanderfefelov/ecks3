"""
   Ecks3 plugin to collect CPU usage information

   Copyright 2011 Chris Read (chris.read@gmail.com)
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

""" This is a plugin to be loaded by Ecks3

return a tuple containing cpu_load for each CPU found

"""


def get_win_cpu(parent, host, port, community):
    oid = (1, 3, 6, 1, 2, 1, 25, 3, 3, 1, 2)  # HOST-RESOURCES-MIB::hrProcessorLoad
    data = parent.get_snmp_data(host, port, community, oid, 1)
    if data:
        return tuple([int(load) for (oid, num, load) in data])
