import os
import hashlib
import sys
import time

baselines = r"C:\Users\HP\OneDrive\Desktop\Baselines"

def Calculate_File_Hash(filepath):
    filename=str(monitoring_dir + "/"+ filepath)
    sha=hashlib.sha512()
    with open(filename, 'rb')as file:
        while True:
            data=file.read(65536)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()

def Check_Integrity(path):
    filepath_filehash_dict = {}
    with open(path, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            filepath = line.split('.')[0]
            filehash = line.split('.')[1]
            filepath_filehash_dict[filepath] = filehash

    while True:
        time.sleep(1)
        for entry in filepath_filehash_dict:
            if os.path.isfile(monitoring_dir + entry) == False:
                print("A file has been DELETED  " + entry)




        for f in os.listdir(monitoring_dir):
            hash = calculate_file_hash(f).split('|')[1]
            if  (f not in filepath_filehash_dict):
                print("A new file has been CREATED  " + f)



            elif hash != filepath_filehash_dict[f]:
                print("A file has been MODIFIED   " + f)


if len(sys.argv)==2:
    if (os.path.isdir(sys.argv[1]) == False):
        print("[ERROR]: Directory does not exit.\nExiting Program....")
        sys.exit()
    else:
        monitoring_dir = sys.argv[1]
elif (len(sys.argv) > 2):
    print("[ERROR]: Too many arguments!!!")
    sys.exit()
else:
    monitoring_dir = os.getcwd()

print("[INFO]: This is the monitoring directory : " + monitoring_dir)
bl_path= os.path.join(monitoring_dir, '.baseline.txt')


choice=input("Choose an option from below:\n 1) Create a new baseline\n 2)Use an existing baseline\n")
while True:
    if (choice==1):
        if os.path.isfile(bl_path) == True:
            ans=input("[INFO]: Baseline already exist.\n Do you want to use already existing baseline?(Yes or No)\n")
            while True:
                response=ans.lower()
                if (response=="yes"):
                    Check_Integrity(b1_path)
                    break
                elif(response=="no"):
                    print("[INFO]: Deleting old baselines.")
                    os.remove(bl_path)
                    time.sleep(1.5)
                    print("[INFO]: Creating a new baseline.")
                    f = open(bl_path, 'x')
                    break
                else:
                    ans=input("[ERROR]: Invalid option!! Choose from 'yes' or 'no':\n")
                    continue
        else:
            f = open(bl_path, "x")
        files = [
            f for f in os.listdir(monitoring_dir)
            if os.path.isfile(os.path.join(monitoring_dir, f))
        ]
        f = open(bl_path, "a")
        for entry in files:
            f.write(calculate_file_hash(entry))
        break

    elif (choice==2):
        Check_Integrity(b1_path)
        break

    else:
        choice=input("[ERROR]: Invalid option!! Choose from '1' or '2'")
        continue
