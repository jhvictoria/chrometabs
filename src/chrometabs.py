import os
import sys
import webbrowser
from subprocess import Popen, PIPE
import json

# MacOS Chrome path
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

def run_this_scpt(scpt, args=[]):
     p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
     stdout, stderr = p.communicate(scpt)
     return stdout

def new_chrome_window():
    """
    Runs Apple script to get new chrome window
    """
    run_this_scpt("""
        tell application "Google Chrome"
            make new window
            activate
        end tell
    """)

def is_file_format(my_file, format):
    if len(my_file.split(".")) >= 2:
        if my_file.split(".")[-1] == format:
            return True
    return False

def do_scan_files(base_path):
    def scan_file(path):
        if is_file_format(path, 'json'):
            try:
                load_json(path)
            except:
                return None
        else:
            return None
        return path

    #Check if path is a single file
    if os.path.isfile(base_path):
        jfile = scan_file(base_path)
        return [jfile]
    
    files = []

    for item in os.listdir(base_path):
        new_path = base_path + item

        #exclude .git folder
        if item == ".git":
            continue

        if os.path.isfile(new_path):
            jfile = scan_file(new_path)
            if jfile == None:
                continue

            files.append(jfile)

        elif os.path.isdir(new_path):
            files = files + do_scan_files(new_path + "/")
    return files

def load_json(json_file):
    try:
        with open(json_file) as f:
            return json.load(f)
    except Exception as e:
        print (e)
        raise e


if __name__ == '__main__':
    print 'chrometabs',len(sys.argv)

    files = list()

    #Setup files to scan
    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            json_path = "tabs/"
        else:  
            print "Usage: python python src/chrometabs.py [path|json]"
            exit(2)
    else:       
        json_path = sys.argv[1]

    #Attach absolute path
    path = os.path.dirname(os.path.abspath(__file__)) + "/"
    json_path = path + json_path

    files = do_scan_files(json_path)

    for f in files:
        try:
            f_json = load_json(f)
        except:
            continue

        if f_json == None:
            continue

        new_chrome_window()
        for name in sorted(f_json, key=f_json.get, reverse=False):
            url = f_json[name]
            print "%s => %s" % (name, url)
            webbrowser.open(url)
        print
