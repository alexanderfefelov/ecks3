"""
    Ecks3 plugin to collect system memory usage information

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


def __calc_size(block_size, block_count):
    return block_size * block_count


def get_win_memory(parent, host, port, community):
    """ This is a plugin to be loaded by Ecks3

        return a tuple containing (total_swap, avail_swap, total_real, avail_real). Values are in kilobytes
    """
    oid = (1, 3, 6, 1, 2, 1, 25, 2, 3, 1)  # HOST-RESOURCES-MIB::hrStorageEntry ??? TODO
    data = parent.get_snmp_data(host, port, community, oid, 1)

    if not data:
        return

    all_blocks = list(
        map(
            parent._build_answer,
            [t[-1] for t in parent._extract(data, tuple, 2)],
            parent._extract(data, str, 3),
            list(map(__calc_size, parent._extract(data, int, 4), parent._extract(data, int, 5))),
            list(map(__calc_size, parent._extract(data, int, 4), parent._extract(data, int, 6)))
        )
    )

    total_swap = 0
    avail_swap = 0
    total_real = 0
    avail_real = 0

    for (typ, label, total, used) in all_blocks:
        if typ == 2:
            total_real = total
            avail_real = total - used
        elif typ == 3:
            total_swap = total
            avail_swap = total - used

    return total_swap, avail_swap, total_real, avail_real
