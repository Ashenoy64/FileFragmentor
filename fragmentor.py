import os
import math


class FileFragmentor:
   

    def makeConfig(self,File,extention,fileName,FileSize,FileCount):
        return "File:"+File+'\n'+ "extention:"+extention+'\n'+   "name:"+fileName+'\n' + "size:"+str(FileSize)+'\n'+ "count:"+str(FileCount)+'\n'
    
    def fragment(self,File_path,size=20):
        try:
            File = os.path.basename(File_path)
            fileName,extention=File.split('.')
            size=size*1024*1024
            FileSize=os.path.getsize(File_path)
        except:
            return 'Incorrect File Path'
        

        
        config=""

        try:
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

                config=self.makeConfig(File,extention,fileName,FileSize,fileCount)
            
            with open(fileName+'/config.txt','wb+') as file:
                file.write(config.encode())

            return f'Successfull, total fragments {fileCount}'
        except:
            return "Something went wrong.."

    def merge(self,dirPath):
        config=''
        try:
            with open(dirPath+'/config.txt','r') as f:
                config=f.read()
        except:
            return "Either Directory doesnt exist or config.txt is missing"
        

        config=config.split('\n')
        
        _,File=config[0].split(':')
        _,extention=config[1].split(':')
        _,name=config[2].split(':')
        _,size=config[3].split(':')
        _,count=config[4].split(':')
        size=int(size)
        count=int(count)
        try:
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
                return "Fragments are corrupted"

            else:
                return "Successfull.."
            
        except:
            return "Something went wrong"









    


if __name__=="__main__":
    print("Make sure to have required file/folder to be in the same directory as this program.")
    wish=int(input("1. Fragment file\n2. Reassmble file\nEnter the Number : "))
    Object=FileFragmentor()
    if wish==1:
        File=input("Enter filename : ")
        size=int(input("Enter the size of fragmented file (MB) : "))
        try:
            Object.fragmentor(File,size)
            print("Successfull")
        except:
            print("Invalid File Path or Size")
    elif wish==2:
        Folder=input("Enter name of fragmeted folder : ")
        try:
            Object.join(Folder)
        except:
            print("Invalid path to folder")
    else:
        print("Invalid Input")
    pass