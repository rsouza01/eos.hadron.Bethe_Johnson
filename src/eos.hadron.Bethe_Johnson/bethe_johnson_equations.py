# eos.hadron.Bethe_Johnson - Bethe & Johnson EOS (Shapiro, pg 211)
# Copyright (C) 2016 Rodrigo Souza <rsouza01@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

import math
import numpy as np


class BJEoSParameters:

    def __init__(self, n_b_from, n_b_to, total_points, nuclear_units):

        self.n_b_from = n_b_from
        self.n_b_to = n_b_to
        self.total_points = total_points
        self.nuclear_units = nuclear_units


class BJEoS:
    """ Bethe & Johnson Equation of State. """

    def __init__(self, parameters):

        self.__parameters = parameters
        self.__a = 1.54
        self._m_neutron = 939.565  # MeV c2
        # self.__light_speed = 2.998e23  # fm s-1
        self.__light_speed = 1


    def energy_density(self, n):
        return 236. * n**(self.__a+1) + self._m_neutron * self.__light_speed * n

    def pressure(self, n):
        return 364. * n**(self.__a + 1)

    def run(self):

        n_b_bin = np.linspace(self.__parameters.n_b_to,
                              self.__parameters.n_b_from,
                              self.__parameters.total_points)

        mev_to_erg = 1.6021773e-6
        fm3_to_cm3 = 1e-39

        format_string = "{}, {}, {}, {}"

        if not self.__parameters.nuclear_units:
            print("# epsilon [erg/cm^3], pressure [erg/cm^3], baryonic_density [1/cm^3], chem_potential[erg]")
            format_string = "{:08e}, {:08e}, {:08e}, {:08e}"

        else:
            print("# epsilon [MeV/fm^3], pressure [MeV/fm^3], baryonic_density [1/fm^3], chem_potential[MeV]")

        for n_b in n_b_bin:

            baryonic_density = n_b

            epsilon = self.energy_density(n_b)
            pressure = self.pressure(n_b)


            # chem_potential = (epsilon + pressure) / baryonic_density
            chem_potential = float((float(epsilon) + float(pressure)) / float(baryonic_density))

            # Convert to erg, grams, cm, etc...
            if not self.__parameters.nuclear_units:

                epsilon *= mev_to_erg/fm3_to_cm3
                pressure *= mev_to_erg/fm3_to_cm3
                baryonic_density *= 1./fm3_to_cm3
                chem_potential *= mev_to_erg

            print(format_string.format(epsilon, pressure, baryonic_density, chem_potential))
