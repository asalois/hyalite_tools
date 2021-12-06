from mako.template import Template
my_tmpl = Template(filename='slurm_c_tmpl.txt')
my_scp_tmpl = Template(filename='to_hyalite_tmpl.txt')
memory = 1024
time = 400
partition = "classpart"
j_name = "PAM"
n_nodes = 1
usr = "v16b915"
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/pthreads"

end = 40
for i in range(end + 1):
    lines = my_tmpl.render(mem=memory, time=time, queue=partition, job_name=j_name,
                           start=1, end=100, num=i, tasks=i, nodes=n_nodes)
    lines += "\n"
    file_name = "pam_sim_" + str(i).zfill(2) + ".slurm"
    file = open(file_name, "w+")
    file.writelines(lines)
    file.close()
    script_lines += "sbatch " + file_name + "\n"


file = open("launch.sh", "w+")
file.writelines(script_lines)
file.close()

file = open("to_hyalite.sh", "w+")
scp = my_scp_tmpl.render(user_id=usr, path=x_dir, file_name="*.slurm launch.sh")
file.writelines(scp)
file.close()
