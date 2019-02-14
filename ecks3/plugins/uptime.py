"""
    Ecks3 plugin to collect system uptime

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


def get_uptime(parent, host, port, community):
    """ This is a plugin to be loaded by Ecks3

        return the number of TimeTicks (100ths of a second) since the system was booted

        Note: This plugin now corrects the bad uptime value returned in
              Windows builds < 7600 (Win 2008 R2)

              See the following for more info:
                  http://fixunix.com/snmp/64367-re-interpreting-hrsystemuptime.html
                  http://forums.cacti.net/about22137.html&highlight=
                  http://web.archiveorange.com/archive/v/WnPpStN7UOuJhcUk5J0T
    """
    import re

    oid = (1, 3, 6, 1, 2, 1, 25, 1, 1)  # HOST-RESOURCE-MIB::hrSystemUptime
    data = parent.get_snmp_data(host, port, community, oid, 1)

    if data:
        # Got some data, let's check the OS now...   
        os = parent.get_os(host, port, community)
        # If it's Windows, check the build...
        if ("Windows" in os) and (int(re.search(r"\(Build (\d+)", os).groups()[0]) < 7600):
            return int(data[0][2]) / 10
        else:
            return int(data[0][2])
    else:
        return None
