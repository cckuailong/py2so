import getopt
import os, sys
import platform


def transfer(dir_pref):
    os_name = ''
    os_info = platform.dist()
    if os_info:
        os_name = os_info[0]
    else:
        print("Cannot Fetch the OS")
        sys.exit(1)
    if not os_name:
        print("Cannot Fetch the OS Name")
        sys.exit(1)
    if os_name.lower() == "ubuntu":
        os.system('cython3 -2 %s.py;'
                'gcc -c -fPIC -I/usr/include/python3.%s/ %s.c -o %s.o'
                % (dir_pref, p_subv, dir_pref, dir_pref))
    elif os_name.lower() == "centos":
        os.system('cython -2 %s.py;'
                'gcc -c -fPIC -I/usr/include/python3.%sm/ %s.c -o %s.o'
                % (dir_pref, p_subv, dir_pref, dir_pref))
    os.system('gcc -shared %s.o -o %s.so' % (dir_pref, dir_pref))
    if clear:
        os.system('rm -f %s.c %s.o %s.py' % (dir_pref, dir_pref, dir_pref))
    else:
        os.system('rm -f %s.c %s.o' % (dir_pref, dir_pref))

if __name__ == '__main__':
    help_show = '''
py2so_py3 is tool to change the .py to .so, you can use it to hide the source code of py
It can be called by the main func as "from module import * "
py2so_py3 needs the environment of python3

Usage: python py2so_py3.py [options] ...

Options:
  -v,  --version    Show the version of the py2so_py3
  -h,  --help       Show the help info
  -p,  --py         Python subversion, default value == 6
                    Example: -p 6  (means you use python3.6)
  -d,  --directory  Directory of your project (if use -d, you change the whole directory)
  -f,  --file       File to be transfered (if use -f, you only change one file)
  -c,  --clear      Clear the origin .py
                    (Warning: the option will delete the .py, but don't be so serious, py2so_py3 will give the project a copy)
  -m,  --maintain   List the file or the directory you don't want to transfer
                    Note: The directories should be surrounded by '[]', and must be the relative path to -d's value 
                    Example: -m __init__.py,setup.py,[poc,resource,venv,interface]

Example:
  python py2so_py3.py -f test_file.py
  python py2so_py3.py -d test_dir -m __init__.py,setup.py,[poc/,resource/,venv/,interface/] -c
    '''
    clear = 0
    p_subv = '6'
    root_name = ''
    file_name = ''
    m_list = ''
    try:
        options,args = getopt.getopt(sys.argv[1:],"vhp:d:f:cm:",["version","help","py=","directory=","file=","clear","maintain="])
    except getopt.GetoptError:
        print('Get options Error')
        print(help_show)
        sys.exit(1)

    for key, value in options:
        if key in ['-h', '--help']:
            print(help_show)
        elif key in ['-v', '--version']:
            print('py2so_py3 version 0.0.1')
        elif key in ['-p', '--py']:
            p_subv = value
        elif key in ['-c', '--clear']:
            clear = 1
        elif key in ['-d', '--directory']:
            root_name = value
        elif key in ['-f', '--file']:
            file_name = value
        elif key in ['-m', '--maintain']:
            m_list = value
            file_flag = 0
            dir_flag = 0
            if m_list.find(',[') != -1:
                tmp = m_list.split(',[')
                file_list = tmp[0]
                dir_list = tmp[1:-1]
                file_flag = 1
                dir_flag = 1
            elif m_list.find('[') != -1:
                dir_list = m_list[1:-1]
                dir_flag = 1
            else:
                file_list = m_list.split(',')
                file_flag = 1
            if dir_flag == 1:
                dir_tmp = dir_list.split(',')
                dir_list=[]
                for d in dir_tmp:
                    if d.startswith('./'):
                        dir_list.append(d[2:])
                    else:
                        dir_list.append(d)

    if root_name != '':
        if not os.path.exists(root_name):
            print('No such Directory, please check or use the Absolute Path')
            sys.exit(1)
        if os.path.exists('%s_old' % root_name):
            os.system('rm -rf %s_old' % root_name)
        os.system('cp -r %s %s_old' % (root_name, root_name))
        try:
            for root, dirs, files in os.walk(root_name):
                for file in files:
                    if m_list != '':
                        skip_flag = 0
                        if dir_flag == 1:
                            for dir in dir_list:
                                if (root+'/').startswith(root_name + '/' + dir):
                                    skip_flag = 1
                                    break
                            if skip_flag:
                                continue
                        if file_flag == 1:
                            if file in file_list:
                                continue
                    pref = file.split('.')[0]
                    dir_pref = root + '/' + pref
                    if file.endswith('.pyc'):
                        os.system('rm -f %s' % dir_pref+'.pyc')
                    elif file.endswith('.so'):
                        pass
                    elif file.endswith('.py'):
                        transfer(dir_pref)
        except Exception as err:
            print(err)
            if "Python.h" in str(err):
                print("Please check out the Python version You use, and use option -p to specify the definite version")
    if file_name != '':
        try:
            dir_pref = file_name.split('.')[0]
            transfer(dir_pref)
        except Exception as err:
            print(err)

