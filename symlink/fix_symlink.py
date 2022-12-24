from genericpath import isfile
import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--target-dir", "-d", required=True, help="The target directory")
parser.add_argument("--all", "-a", default=False, action='store_true', help="Fix all symlinks")
args = parser.parse_args()
target_dir = args.target_dir

cwd = os.getcwd()
print(cwd)
if target_dir.find(cwd) < 0:
    target_dir = os.path.join(cwd, target_dir)
print("Target dir: {}\n".format(target_dir))


def lsdir(dir):
    popen = subprocess.Popen(['ls', '-l', '--color', dir], stdout=subprocess.PIPE)
    for line in popen.stdout.readlines():
        print(line.decode().strip())


def fix_symlinks(dir):
    print(dir)
    os.chdir(dir)
    for f in os.listdir(dir):
        if not os.path.islink(f) and 'lib' in f:
            parts = f.split('.')
            try:
                int(parts[-1])
            except:
                continue
            while parts[-1] != 'so':
                link = '.'.join(parts[:-1])
                try:
                    # Remove bad symlink
                    if os.path.islink(link):
                        os.unlink(link)

                    # Create good symlink
                    if not os.path.isfile(link):
                        os.symlink(f, link)
                    parts = parts[:-1]
                except Exception as ex:
                    raise ex


def get_origin(link):
    popen = subprocess.Popen(['git', 'diff', link], stdout=subprocess.PIPE)
    lines = popen.stdout.readlines()
    origin = ""
    if len(lines) > 5:
        origin = lines[5]
    if len(origin) > 0 and origin[0] == '-':
        return origin[1:].strip()
    else:
        return None

def fix_git_symlinks(dir):
    print(dir)
    os.chdir(dir)
    for f in os.listdir(dir):
        if os.path.islink(f):
                link = f
                origin = get_origin(link)
                if origin:
                    os.unlink(link)
                    os.symlink(origin, link)


########################################################################
if __name__ == "__main__":
    if args.all:
        for subdir in os.listdir(target_dir):
            full_path_subdir = os.path.join(target_dir, subdir)
            if os.path.isdir(full_path_subdir):
                libdir = os.path.join(full_path_subdir, "lib")
                if os.path.isdir(libdir):
                    fix_git_symlinks(libdir)
                    lsdir(libdir)
    else:
        fix_git_symlinks(target_dir)
        lsdir(target_dir)

