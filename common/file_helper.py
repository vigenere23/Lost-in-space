import sys
import os

def get_path(scriptfile, filename):
  return os.path.join(os.path.dirname(scriptfile), filename)