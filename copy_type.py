#codding=utf-8
import os
import glob
import shutil
import argparse


def copy(file_list, src, dst):
    count = 0
    for f in file_list:
        if count % 1000 ==0:
           print("{}/{}".format(count,len(file_list)))
        print(f)
        src_file = src + "/" + f
        dst_file = dst + "/" + f
        print(dst_file)
        shutil.copyfile(src_file, dst_file)
        count += 1
    
def getTypeFileList(src, type):
    files = glob.glob(os.path.join(src, "*.{}".format(type)))
    file_list = []
    for f in files:
        f = f.replace(src+"/", "")
        # print(f)
        file_list.append(f)
        # print(f)
    # pass
    return file_list

def getFileList(src):
    file_list = []
    for root, dirs, files in os.walk(src):
        print(root)
        print(files)
        for f in files:
            # file_name = root + "/" + f
            file_name = f
            file_list.append(file_name)
            print(file_name)
    return file_list
       
def main():
    parser = argparse.ArgumentParser(description="copy.py --src --dst ")
    parser.add_argument("--src", type=str, default = None)
    parser.add_argument("--dst", type=str, default = None)
    parser.add_argument("--t", type=str, default = None)
    args = parser.parse_args()
    src = args.src
    dst = args.dst
    print(args.t)
    if args.t==None:
        file_list = getFileList(src)
    else:
        file_list = getTypeFileList(src, args.t)
    copy(file_list, src, dst)

if __name__ == "__main__":
    main()
