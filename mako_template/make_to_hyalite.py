from mako.template import Template
my_scp_tmpl = Template(filename='to_hyalite_tmpl.txt')
usr = 'v16b915'
file_nm = '*slurm'
to_path = '/mnt/lustrefs/scratch/' + usr + '/'

file = open("to_hyalite.sh","w+")
scp = my_scp_tmpl.render(user_id=usr, path=to_path, file_name=file_nm)
file.writelines(scp)
file.close()
