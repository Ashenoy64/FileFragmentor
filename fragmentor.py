import os
import math


def makeConfig(File,exetention,fileName,FileSize,fileCount):
    return "File:"+File+'\n'+ "extention:"+exetention+'\n'+   "name:"+fileName+'\n' + "size:"+str(FileSize)+'\n'+ "count:"+str(fileCount)+'\n'
    



def fragmentor(File,size=25):
    fileName,extention=File.split('.')
    size=size*1024*1024
    FileSize=os.path.getsize(File)
    config=""

    if not os.path.exists(fileName):
        os.makedirs(fileName)

    with open(File,"rb") as file:
        chunck=0
        fileCount=0

        data=file.read(size)

        while data:
            output_file=os.path.join(fileName,f"{fileName}{fileCount}.fg")
            with open(output_file,'wb') as f:
                f.write(data)

                chunck+=1
                fileCount+=1
                data=file.read(size)

        config=makeConfig(File,extention,fileName,FileSize,fileCount)
    
    with open(fileName+'/config.txt','wb+') as file:
        file.write(config.encode())


def join(dirPath):
    config=''
    with open(dirPath+'/config.txt','r') as f:
        config=f.read()

    config=config.split('\n')
    
    _,File=config[0].split(':')
    _,extention=config[1].split(':')
    _,name=config[2].split(':')
    _,size=config[3].split(':')
    _,count=config[4].split(':')
    size=int(size)
    count=int(count)

    with open(File,'wb') as f:
        for i in range(count):
            file=os.path.join(dirPath,f"{name}{i}.fg")
            
            try:
                with open(file,"rb") as file:
                    data=file.read()
                    f.write(data)
            except:
                print("File {name}{i}.fg Missing ")
                break


    if(i==count and os.path.getsize(File)!=size):
        print("Fragmented file is corrupted")

    else:
        print("Successfull..")


if __name__=="__main__":
    print("Make sure to have required file/folder to be in the same directory as this program.")
    wish=int(input("1. Fragment file\n2. Reassmble file\nEnter the Number : "))
    
    if wish==1:
        File=input("Enter filename : ")
        size=int(input("Enter the size of fragmented file (MB) : "))
        try:
            fragmentor(File,size)
            print("Successfull")
        except:
            print("Invalid File Path or Size")
    elif wish==2:
        Folder=input("Enter name of fragmeted folder : ")
        try:
            join(Folder)
        except:
            print("Invalid path to folder")
    else:
        print("Invalid Input")
    pass