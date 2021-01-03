import os

folder = ''

for root, folders, files in os.walk('D:\\Manisharma'):
    print()
    # print(root)
    # print(folders)
    
    # print(files)
    for file in files:
        if file[0] == '[':
            print(file)
        
        

    # for folder in folders:
    #     print(folder)
    # os.mkdir(f'D:\\NewFolder\\{folder}')


    # for file in files:
    #     print(folder)
    #     print(file)

    # print()

# os.mkdir("D:\\NewFolder\\")
