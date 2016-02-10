#!/bin/bash

clear

echo "Generating Bethe & Johnson EoS..."
./bethe_johnson_eos.py --r_from=0.1 --r_to=3  > ../generated/bethe_johnson.csv
