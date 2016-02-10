#!/usr/bin/python

# eos.hadron.Bethe_Johnson - Bethe & Johnson EOS (Shapiro, pg 211)
# Copyright (C) 2015 Rodrigo Souza <rsouza01@gmail.com>

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


"""
   bethe_johnson_eos.py - Generates the EoS table.

    History:
    Version 0.1: 2016/02/10     (rsouza) - Creating the file.

    Usage:
        bethe_johnson_eos.py

    Example:
        ./bethe_johnson_eos.py

"""

import sys
import scipy.integrate as integrate
import numpy as np
import bethe_johnson_equations as bjeqs
from datetime import datetime

import sys
import getopt

def usage():
    """
    Shows the program usage
    """
    print(
        "Usage: \n" +
        "    bethe_johnson_eos.py\n")


def get_cl_parameters(argv):
    """
    Extracts the command line parameters.
    :param argv:
    :return:
    """

    n_b_from = 1e-15
    n_b_to = 4000

    try:
        opts, args = getopt.getopt(argv, "hf:t:", ["help", "r_from=", "r_to="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:

        if opt in ("-f", "--r_from"):
            n_b_from = float(arg)

        elif opt in ("-t", "--r_to"):
            n_b_to = float(arg)

        elif opt == '-h':
            usage()
            exit(0)
        else:
            assert False, "Unhandled exception."

    return n_b_from, n_b_to


def main(argv):
    
    n_b_from, n_b_to = get_cl_parameters(argv)

    print("# Bethe & Johnson EoS, , ,")

    parameters = bjeqs.BJEoSParameters(
        n_b_from=n_b_from,
        n_b_to=n_b_to,
        total_points=400,
        nuclear_units=True)
    
    bj_eqs = bjeqs.BJEoS(parameters)
    bj_eqs.run()


if __name__ == "__main__":
    main(sys.argv[1:])
