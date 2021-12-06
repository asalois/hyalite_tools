#!/bin/bash
# check queue
squeue -t r -u `whoami` -S id	
