from mako.template import Template
my_scp_tmpl = Template(filename='from_hyalite_tmpl.txt')
usr = 'v16b915'
file_nm = '*slurm'
from_path = '/mnt/lustrefs/scratch/' + usr + '/'

file = open("from_hyalite.sh","w+")
scp = my_scp_tmpl.render(user_id=usr, path=from_path, file_name=file_nm)
file.writelines(scp)
file.close()
