# Copyright (C) 2016  Red Hat, Inc
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Test cases for the commissaire.oscmd.redhat module.
"""

from . import TestCase
from commissaire.oscmd import redhat


class Test_Red_Hat_OSCmd(TestCase):
    """
    Tests for the OSCmd class for 'Red Hat'.
    """

    def before(self):
        """
        Sets up a fresh instance of the class before each run.
        """
        self.instance = redhat.OSCmd()

    def test_redhat_oscmd_commands(self):
        """
        Verify RHEL's OSCmd returns proper data on restart.
        """
        for meth in ('restart', 'upgrade', 'install_docker',
                     'start_docker', 'install_kube', 'start_kube'):
            cmd = getattr(self.instance, meth)()
            self.assertEquals(list, type(cmd))
