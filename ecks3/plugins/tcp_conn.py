"""
    Ecks3 plugin to collect TCP connection information

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


def __ip_addr(data):
    return ".".join([str(a) for a in data])


def get_tcp_conn(parent, host, port, community):
    """ This is a plugin to be loaded by Ecks3

        return a list of tuples containing (local_addr, local_port, rem_addr, rem_port, state)

        state is an integer which represents the following:
            closed(1),
            listen(2),
            synSent(3),
            synReceived(4),
            established(5),
            finWait1(6),
            finWait2(7),
            closeWait(8),
            lastAck(9),
            closing(10),
            timeWait(11),
            deleteTCB(12)
    """
    oid = (1, 3, 6, 1, 2, 1, 6, 13, 1, 1)  # TCP-MIB::tcpConnState
    data = parent.get_snmp_data(host, port, community, oid, 1)
    return [(__ip_addr(addrs[:4]), addrs[4], __ip_addr(addrs[5:9]), addrs[9], int(state)) for (oid, addrs, state) in data]
