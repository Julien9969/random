import os, time, subprocess, shutil, re

SE_PATTERN = r"S(\d+)E(\d+)"

#  aniDL.exe --service crunchy --auth --username super.mail.woof@gmail.com --password JU02++=02+

# aniDL.exe --service crunchy --series {ID} --allDubs --novids --all --waittime 45000

# aniDL.exe --service crunchy --series GRDV0019R --dlsubs all --novids --all --timeout

# aniDL.exe --service crunchy --series GYP8DP1MY --dlsubs all --novids --all --timeout 20000
try:
    os.mkdir("subs pack")
except:
    pass
aniDL_path = "/home/media/NAS/SUB/cr-links/anidl/aniDL"

print(aniDL_path)
sub = subprocess.Popen(f"{aniDL_path} --service crunchy --auth --username super.mail.woof@gmail.com --password JU02++=02+", shell=True)    
sub.wait()
while True:

    with open("links_2.txt", "r") as f:
        lines = f.readlines()
        first = lines.pop(0)
        f.close()
        
        
    id = first.strip().split("/")[3]
    print(f"\n==================={first}===================\n")

    sub = subprocess.Popen(f"{aniDL_path} --service crunchy --series {id} --allDubs --novids --all --waittime 40000", shell=True)
    # time.sleep(5)
    sub.wait()
    folder = os.listdir("anidl/videos")[0].split(" - ")[0]
    try:
        os.mkdir(f"subs pack/{folder}")
    except:
        pass
    
    all = os.listdir("anidl/videos")
    for files in all:
        match = re.search(SE_PATTERN, files)
        try:
            season = match.group(1)
            episode = match.group(2)
        except:
            season = "Specials"
            episode = ""
        
        print(f"Season: {season} Episode: {episode}")

        if not os.path.exists(f"subs pack/{folder}/Season {season}"):
            os.mkdir(f"subs pack/{folder}/Season {season}")

        if files.endswith("eng.English.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/ENGLISH - Forced"):
                os.mkdir(f"subs pack/{folder}/Season {season}/ENGLISH - Forced")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/ENGLISH - Forced/{files.replace(' [${height}p]', '')}")
        elif files.endswith("eng.English.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/ENGLISH"):
                os.mkdir(f"subs pack/{folder}/Season {season}/ENGLISH")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/ENGLISH/{files.replace(' [${height}p]', '')}")
        elif files.endswith("deu.German.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/GERMAN - Forced"):
                os.mkdir(f"subs pack/{folder}/Season {season}/GERMAN - Forced")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/GERMAN - Forced/{files.replace(' [${height}p]', '')}")
        elif files.endswith("deu.German.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/GERMAN"):
                os.mkdir(f"subs pack/{folder}/Season {season}/GERMAN")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/GERMAN/{files.replace(' [${height}p]', '')}")     
        elif files.endswith("fra.French.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/French - Forced"):
                os.mkdir(f"subs pack/{folder}/Season {season}/French - Forced")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/French - Forced/{files.replace(' [${height}p]', '')}") 
        elif files.endswith("fra.French.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/French"):
                os.mkdir(f"subs pack/{folder}/Season {season}/French")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/French/{files.replace(' [${height}p]', '')}")
        elif files.endswith("ita.Italian.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Italian - Forced"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Italian - Forced")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Italian - Forced/{files.replace(' [${height}p]', '')}") 
        elif files.endswith("fra.Italian.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Italian"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Italian")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Italian/{files.replace(' [${height}p]', '')}")
        elif files.endswith("por.Brazilian Portuguese.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Brazilian - Forced"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Brazilian - Forced")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Brazilian - Forced/{files.replace(' [${height}p]', '')}") 
        elif files.endswith("por.Brazilian Portuguese.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Brazilian"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Brazilian")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Brazilian/{files.replace(' [${height}p]', '')}")
        elif files.endswith("spa-419.Latin American Spanish.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Latin American Spanish - Forced"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Latin American Spanish - Forced")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Latin American Spanish - Forced/{files.replace(' [${height}p]', '')}") 
        elif files.endswith("spa-419.Latin American Spanish.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Latin American Spanish"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Latin American Spanish")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Latin American Spanish/{files.replace(' [${height}p]', '')}")
        elif files.endswith("spa-ES.European Spanish.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/European Spanish - Forced"):
                os.mkdir(f"subs pack/{folder}/Season {season}/European Spanish - Forced")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/European Spanish - Forced/{files.replace(' [${height}p]', '')}") 
        elif files.endswith("spa-ES.European Spanish.cc.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/European Spanish"):
                os.mkdir(f"subs pack/{folder}/Season {season}/European Spanish")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/European Spanish/{files.replace(' [${height}p]', '')}")
        elif files.endswith("ara.Arabic (Saudi Arabia).ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Arabic"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Arabic")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Arabic/{files.replace(' [${height}p]', '')}")
        elif files.endswith("rus.Russian.ass"):
            if not os.path.exists(f"subs pack/{folder}/Season {season}/Russian"):
                os.mkdir(f"subs pack/{folder}/Season {season}/Russian")
            shutil.move(f"anidl/videos/{files}", f"subs pack/{folder}/Season {season}/Russian/{files.replace(' [${height}p]', '')}")
        else:
            os.remove(f"anidl/videos/{files}")
    
    with open("links_2.txt", "w") as f:
        f.writelines(lines)


