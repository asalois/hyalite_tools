#!/bin/bash
# Go to scratch and check queue
cd /mnt/lustrefs/scratch/v16b915/
squeue -u `whoami` -S id
