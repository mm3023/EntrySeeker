


def import_fromjs(request):
    filename="/var/www/html/served_files/"+request.FILES['file'].name+'_'+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    print(filename);
        
    new_file=open(filename,'wb');
    new_file.write(request.FILES['file'].read());
    new_file.close();
     
    os.listdir();
    print(os.listdir());
    print(type(os.listdir()));
