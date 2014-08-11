

import sys
import os
import shutil

app_install_path = '/var/www'

def help():
    print ''
    print 'usage: ' + sys.argv[0] + ' <appname>  [demoname]'
    print ''

def main():
    if len(sys.argv) < 2:
        help()
        exit(0)

    name_app = sys.argv[1]
    if len(sys.argv) > 2:
        name_demo_app = sys.argv[2]
    else:
        name_demo_app = 'dj_demo'

    
    #copy files
    if not os.path.exists(name_demo_app):
        print  name_demo_app + " doesn't exist"
        exit(0)
 
    if os.path.exists(name_app):
        shutil.rmtree(name_app)
        
    shutil.copytree(name_demo_app, name_app)    
    
    process(name_app, name_demo_app, name_app)

    if os.path.isdir(os.path.join(app_install_path, name_app)):
        print 'install failed, aready exist!'
    else: 
        shutil.move(name_app, app_install_path)
        os.chdir(os.path.join(app_install_path, name_app))
        os.system('python init.py')


def process(path, oldname, newname):
    for item in os.listdir(path):
        subpath = os.path.join(path, item)
        
        if os.path.isdir(subpath) and item == '.git':
            shutil.rmtree(subpath)

        if os.path.isfile(subpath):
            fp = open(subpath, 'r+')
            content = fp.read().replace(oldname, newname) 
            fp.seek(0)
            fp.truncate() #clear file content
            fp.write(content)
            fp.close()
        
        if item == oldname:
            newpath = os.path.join(path, newname) 
            shutil.move(subpath, newpath)
            subpath=newpath
            
        if os.path.isdir(subpath):
            process(subpath, oldname, newname)   



if __name__ == '__main__':
    main()

