import datetime;
import os;


def import_fromjs(request):
    filename="/var/www/html/served_files/"+request.FILES['file'].name+'_'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    print(filename);
        
    new_file=open(filename,'wb');
    new_file.write(request.FILES['file'].read());
    new_file.close();
     
    os.listdir();
    print(os.listdir());
    print(type(os.listdir()));


    print("----current dir---",os.getcwd());
    print("----List dir-------",os.listdir());
    print("----permissions W ?--",os.access(os.getcwd(),os.W_OK)); 
    print("end----------")
    return 0;


def fileClear():
    print("begin fileClear()");
    clear_served_files(request):
    print("os.getcwd()--",os.getcwd());
    os.chdir("/var/www/html/served_files")
    print("os.getcwd()--",os.getcwd());
    print("os.listdir() -- ",os.listdir());
    for files in os.listdir() :
        os.remove(files);
    print("os.listdir() -- ",os.listdir());    
        
    #return redirect('clear_served_files()');
    print("end fileClear()");
    return 0;
