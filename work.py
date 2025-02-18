config = {
    'latex2mdpath':'E:\\github\\latex2md\\main.py',
    'inputPath':'E:\\University\\Study\\summarize\\pages',
    # 'outputPath':'D:\\uukuu.github.io\\content\\posts\\数学',
    'outputPath':'E:\\github\\uukuu.github.io\\content\\posts\\auto-math',
}


import os

ntran = ["定理表.tex","main.tex","高等代数"]
print(os.listdir(config['inputPath']))
def workdir(inputPath,path):
    for name in os.listdir(inputPath+"\\"+path):
        if name in ntran:
            continue
        if path != "":
            newpath = inputPath+"\\"+ path + "\\" + name
        else:
            newpath = inputPath+"\\"+name
        # print(newpath)
        if os.path.isdir(newpath):
            if path == "":
                workdir(inputPath,name)
            else:
                workdir(inputPath,path+"\\"+name)
        elif path != "":
            os.system(f'python {config['latex2mdpath']} {newpath} {config['outputPath']+"\\"+path+"\\"+os.path.splitext(name)[0]+".md"}')

workdir(config['inputPath'],"")
# os.system(f'python {config['latex2mdpath']} D:\\Desktop\\大学\\Study\\summarize\pages\复变函数\复平面拓扑\\1.tex')