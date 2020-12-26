import os
import subprocess,platform
hostname = "google.com" #example
# completedp = subprocess.run("ping -a " + hostname,shell=True, check=True,text=True)
# print(completedp.args)
# print(completedp.returncode)
# print(completedp.stdout)
# print(completedp.stderr)

output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', hostname), shell=True)
print(output)
