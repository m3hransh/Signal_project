import re
import sys
import os
s_pattern = re.compile(r'#section:(\w+)')

def make_sec(file_path):
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            section = re.findall(s_pattern, line)
            if section:
                e_pattern = re.compile(r"#endsection")
                line = fp.readline()
                with open(os.path.join('doc/codes',section[0]+'.py'),'w') as fw:
                    while line and not re.findall(e_pattern, line):
                        fw.write(line)
                        line = fp.readline()
            line = fp.readline()
if __name__ == "__main__":
    if len(sys.argv) >1:
        make_sec(sys.argv[1])