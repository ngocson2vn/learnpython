import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="File path", required=True)
args = parser.parse_args()

fread = open(args.file)
for line in fread:
    sockets = line.strip().split(':')
    cmd = 'nc -zv {} {}'.format(sockets[0], sockets[1])
    print(cmd)
    proc = subprocess.Popen(['nc', '-zv', sockets[0], sockets[1]], stdout=subprocess.PIPE)
    print(''.join(proc.stdout.readlines()))

# ls -l --color
popen = subprocess.Popen(['ls', '-l', '--color'], stdout=subprocess.PIPE)
print(''.join(popen.stdout.readlines()))
