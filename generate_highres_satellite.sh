#!/bin/bash
make USER_MOTION_SIZE=20000
./gps-sdr-sim -e brdc0010.22n -u satellite_100_highres.csv -s 2500000 -o satellite_100_highres.bin -i
