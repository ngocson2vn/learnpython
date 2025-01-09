import subprocess as sp

cmd = "while true; do echo 'Hello!'; sleep 1; done"

p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.STDOUT, shell=True, bufsize=1, encoding="utf-8")
for line in p.stdout:
    print(line, end="")
p.stdout.close()
p.wait()
