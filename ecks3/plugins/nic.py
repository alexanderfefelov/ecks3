"""
    Ecks3 plugin to collect network interface information

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


def get_nic(parent, host, port, community):
    """ This is a plugin to be loaded by Ecks3

        Info on the data returned is available at http://www.oidview.com/mibs/0/IF-MIB.html

        return an array of tuples containing (name, type, mtu, speed, mac, admin_status, oper_status,
            last_changed, in_bytes, in_u_pkts, in_nu_pkts, in_discard, in_err, in_unknown,
            out_bytes, out_u_pkts, out_nu_pkts, out_discard, out_err, out_queue) for each ethernet interface

        The type return value is an integer that can be looked up at http://www.iana.org/assignments/ianaiftype-mib

        Most common type is 6 (ethernet)
    """
    oid = (1, 3, 6, 1, 2, 1, 2, 2, 1)  # IF-MIB::ifEntry
    data = parent.get_snmp_data(host, port, community, oid, 1)

    return list(
        map(
            parent._build_answer,
            parent._extract(data, str, 2),   # Name
            parent._extract(data, int, 3),   # ifType
            parent._extract(data, int, 4),   # MTU
            parent._extract(data, int, 5),   # Speed
            parent._extract(data, str, 6),   # MAC
            parent._extract(data, int, 7),   # Admin Status
            parent._extract(data, int, 8),   # Oper Status
            parent._extract(data, int, 9),   # Last Change
            parent._extract(data, int, 10),  # In Bytes
            parent._extract(data, int, 11),  # In Unicast Pkts
            parent._extract(data, int, 12),  # In Not Unicast Pkts
            parent._extract(data, int, 13),  # In Discards
            parent._extract(data, int, 14),  # In Errors
            parent._extract(data, int, 15),  # In Unknown Protocols
            parent._extract(data, int, 16),  # Out Bytes
            parent._extract(data, int, 17),  # Out Unicast Pkts
            parent._extract(data, int, 18),  # Out Not Unicast Pkts
            parent._extract(data, int, 19),  # Out Discards
            parent._extract(data, int, 20),  # Out Errors
            parent._extract(data, int, 21),  # Out Queue Length
        )
    )
