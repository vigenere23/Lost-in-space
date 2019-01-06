import sys
import os

def get_path(filename):
  root = os.path.join(os.path.dirname(__file__), "../..")
  return os.path.join(os.path.dirname(root), filename)