"""This file wraps pacman functions to python functions"""

from subprocess import check_call as ccall
import time
import shutil
import logging
from tempfile import NamedTemporaryFile

PACCONF = "./pacman.conf"

logging.basicConfig(format='%(asctime)s %(message)s',  level="DEBUG")

def backup_configuration_file():
    shutil.copy2(PACCONF,  "".join((PACCONF, str(int(time.time())),"~")))
    logging.debug("Created backup file of pacman.conf")

def install(packagename):
    ccall(["pacman", "-Ss",  "--noconfirm",  packagename])
    logging.info("installed {}".format(packagename))
    
def pac_conf_edit(repo,  enable_repo=True):
    try:
        edit_next=False # because alwasys two lines have to be edited
        with NamedTemporaryFile(delete=False) as tmp_f, open(PACCONF) as f:
            for line in f:
                if edit_next:
                    if enable_repo:
                        tmp_f.write(line[1:])
                    else:
                        tmp_f.write("".join(("#", line)))
                    logging.info("changed {}".format(line))
                    edit_next = False
                    continue
                if enable_repo and line.startswith("".join(["#[",repo])): 
                    tmp_f.write(line[1:]) #remove the #, thus enabling the repo
                    logging.info("changed {}".format(line))
                    edit_next = True
                elif line.startswith("".join(("[",  repo))):
                    tmp_f.write("".join(("#", line) ))
                    logging.info("changed {}".format(line))
                    edit_next = True
                else:
                    tmp_f.write(line)
                    
        shutil.move(tmp_f.name,  f.name)
    except EnvironmentError:
        logging.execption("Something went terribly wrong. Do we have the right permissions?")
