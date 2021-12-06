from mako.template import Template
my_tmpl = Template(filename='slurm_matlab_tmpl.txt')
my_scp_tmpl = Template(filename='to_hyalite_tmpl.txt')
memory = 8 * 1024
time = 400
partition = "classpart"
m_fun = "scan_dfe"
j_name = "ber"
n_task = 2
n_nodes = 1
usr = "v16b915"
script_lines = "#!/bin/bash \n"
x_dir = "/mnt/lustrefs/scratch/v16b915/dfe_scan_new/"

end = 6
for i in range(end + 1):
    lines = my_tmpl.render(mem=memory, time=time, queue=partition, job_name=j_name,
                           start=1, end=1000, limit=100, num=i, tasks=n_task, nodes=n_nodes, matlab_func = m_fun)
    lines += "\n"
    file_name = "dfe_ber_" + str(i).zfill(2) + ".slurm"
    file = open(file_name, "w+")
    file.writelines(lines)
    file.close()
    script_lines += "sbatch " + file_name + "\n"


file = open("launch.sh", "w+")
file.writelines(script_lines)
file.close()

file = open("to_hyalite.sh", "w+")
scp = my_scp_tmpl.render(user_id=usr, path=x_dir, file_name="*.slurm")
file.writelines(scp)
file.close()
