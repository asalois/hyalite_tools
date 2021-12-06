#!/bin/bash
sacct  --format="JobID,JobName,AllocCPUS,state,Elapsed,MaxVMSize,MaxRSS"
