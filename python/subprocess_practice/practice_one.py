import os, sys
import subprocess

from glob import glob
from pprint import pprint

tar_dir = 'C:/Program Files (x86)/DAUM/PotPlayer'
runcher = 'PotPlayer.exe'

file_path = 'D:/잡/영화/봄날은간다.mkv'


subprocess.Popen(f"{os.path.join(tar_dir, runcher)} {file_path}")


