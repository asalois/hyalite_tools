# hyalite_tools
Some scripts and tools I use for Hyalite HPC

## scripts
* **go_to_scratch.sh** - if sourced it will go to scratch folder
* **show_me_jobs.sh** - shows the current running and pending jobs for your user sorted by ID 
* **show_me_jobs_no_pending.sh** - shows the current running jobs only for your user sorted by ID 
* **show_usage.sh** - shows the resources used by your recent completed jobs

## mako_template
* Use make_matlab_slurms.py to make matlab sbatch scripts
    * this creates a number of ".slurm" files
    * also creates a launch.sh file that will launch all the created ".slurm" files
    * also creates a to_hyalite.sh script to copy the ".slurm" to hyalite   