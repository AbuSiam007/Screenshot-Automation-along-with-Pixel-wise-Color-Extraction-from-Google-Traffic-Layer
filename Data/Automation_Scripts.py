from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import datetime
from selenium.webdriver.chrome.options import Options
opt = Options()
from PIL import Image
import csv
import datetime
from numpy import size
from scipy.spatial import KDTree
from webcolors import (
    css3_hex_to_names,
    hex_to_rgb,
)
def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []    
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)    
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'

def current_datetime():
    return datetime.datetime.now().strftime("%Hh_%Mm_%Ss , %d-%m-%Y")


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"


opt = webdriver.ChromeOptions()
opt.headless =  True
opt.add_argument("--window-size=1920,1080")
opt.add_argument('--ignore-certificate-errors')
opt.add_argument(f'user-agent={user_agent}')
opt.add_argument('--allow-running-insecure-content')
opt.add_argument("--disable-extensions")
opt.add_argument("--proxy-server='direct://'")
opt.add_argument("--proxy-bypass-list=*")
opt.add_argument("--start-maximized")
opt.add_argument('--disable-gpu')
opt.add_argument('--disable-dev-shm-usage')
opt.add_argument('--no-sandbox')
opt.add_argument("--hide-scrollbars")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)


main = []
mainrows = []
row = []
temprow = []
rows = []
temp = 0

def pixtocolor(coordinate,node):
    # print(image.getpixel(coordinate))
    r,g,b,a = image.getpixel(coordinate)
    if((90 <= r <= 147) and (210 <= g <= 230)and (100 <= b <= 156)):
        # print("green")
        return 0
    elif((245 <= r <= 256) and (140 <= g <= 189)and (70 <= b <= 139)):
        # print("yellow")
        return 1
    elif((235 <= r <= 249) and (50 <= g <= 130)and (40 <= b <= 120)):
        # print("red")
        return 2
    elif((122 <= r <= 170) and (10 <= g <= 120)and (20 <= b <= 120)):
        # print("deep red")
        return 3
    elif((200 <= r <= 232) and (223 <= g <= 235)and (210 <= b <= 240)):
        # print("grey")
        return 0
    else:
        return 0
        #-----------------------------------------------
        #for debugging purpose
        # print("Not in Range")
        # print(node)
        # print(coordinate)
        # print(image.getpixel(coordinate))
        # print(convert_rgb_to_names((r,g,b)))
        #-----------------------------------------------
nodes = {
    "AB" : [(995,206),(932,226),(874,244),(812,262),(754,269),(699,265),(650,258)],
    "BA" : [(995,195),(931,215),(874,233),(812,252),(754,259),(699,254),(650,247)],

    "BC" : [(608,252),(562,245),(514,238),(462,231)],
    "CB" : [(608,242),(562,235),(514,228),(462,220)],

    "CD" : [(410,223),(356,215)],
    "DC" : [(410,213),(356,205)],

    "DE" : [(321,244),(312,302),(303,358)],
    "ED" : [(307,244),(297,302),(289,358)],

    "EF" : [(294,416),(285,475),(275,543)],
    "FE" : [(281,416),(271,475),(260,543)],

    "FG" : [(271,624),(253,694),(241,754),(235,819),(224,894),(215,956)],
    "GF" : [(247,624),(237,694),(228,754),(219,819),(204,894),(194,956)],

    "GH" : [(231,982),(300,985),(363,988),(420,993),(467,996),(520,1000),(577,1007),(636,1017),(694,1025),(750,1027),(817,1025),(890,1023),(960,1022),(1027,1024),(1105,1026)],
    "HG" : [(231,995),(300,996),(363,999),(420,1004),(467,1007),(520,1011),(577,1019),(636,1029),(694,1037),(750,1039),(817,1038),(890,1035),(960,1035),(1027,1036),(1105,1036)],

    "HK" : [(1205,1016),(1260,1017),(1324,1012),(1373,1007),(1440,996),(1500,1000),(1555,1003),(1610,1006)],
    "KH" : [(1202,1027),(1260,1028),(1324,1022),(1373,1017),(1440,1007),(1500,1010),(1555,1014),(1610,1017)],

    "KJ" : [(1637,979),(1642,922),(1646,857),(1645,776),(1634,704),(1627,648),(1619,594),(1610,533),(1599,468),(1587,393),(1574,318),(1565,262),(1555,204),(1544,147),(1531,72)],
    "JK" : [(1650,979),(1654,922),(1656,857),(1655,776),(1647,702),(1638,648),(1631,594),(1622,533),(1612,468),(1599,393),(1586,318),(1576,262),(1566,204),(1556,147),(1543,75)],

    "JA" : [(1483,29),(1415,49),(1357,73),(1290,100),(1228,122),(1172,140),(1122,156),(1074,170)],
    "AJ" : [(1483,17),(1411,38),(1351,61),(1288,88),(1226,110),(1172,127),(1118,144),(1072,158)],

    "BL" : [(620,284),(610,345),(603,400)],
    "LB" : [(615,284),(605,345),(598,400)],

    "CN" : [(431,260),(423,312),(414,374)],
    "NC" : [(426,260),(418,312),(408,374)],

    "EN" : [(335,384),(386,392)],
    "NE" : [(335,393),(386,401)],

    "NM" : [(448,404)],
    "MN" : [(448,414)],

    "ML" : [(510,413),(570,422)],
    "LM" : [(510,423),(570,431)],
    
    "FM" : [(293,582),(338,587),(393,595),(443,603),(456,558),(466,500),(477,429)],
    "MF" : [(293,586),(338,592),(393,600),(443,608),(461,558),(471,500),(479,445)],

    "AH" : [(1063,226),(1081,283),(1098,337),(1114,385),(1138,453),(1151,511),(1168,586),(1178,650),(1183,719),(1185,786),(1182,842),(1177,891),(1172,931),(1165,994)],
    "HA" : [(1048,226),(1067,283),(1085,337),(1102,390),(1125,453),(1138,513),(1155,589),(1166,650),(1171,719),(1171,786),(1169,842),(1164,891),(1159,931),(1154,994)]

}


for i in range(1):

    driver.get("http://localhost:8080/")
    sleep(5)

    #Removing for educational purposes only
    driver.execute_script("""
        var l = document.getElementsByClassName("gm-style")[0];
    
        l.removeChild(l.childNodes[16]);
        l.removeChild(l.childNodes[14]);
    """)

    currentdatetime = current_datetime()
    filename = "Screenshots\screenshot "+currentdatetime+".png"
    driver.get_screenshot_as_file(filename)
    print("Taking Screenshot "+str(i)+" at "+currentdatetime)


    image = Image.open(filename)
    main.append(currentdatetime)
    for node,coos in nodes.items():
        for coo in coos:
            colorvalue = pixtocolor(coo,node)
            temp = temp + colorvalue
            row.append(colorvalue)

        temprow = row.copy()
        rows.append(temprow)
        temp = temp/(len(coos)*3)
        main.append(temp)
        temp = 0

    tempmain = main.copy()
    mainrows.append(tempmain)
    main.clear()

    del image


fields = ['Date Time', 'AB', 'BA', 'BC', 'CB', 'CD', 'DC', 'DE', 'ED', 'EF', 'FE', 'FG', 'GF', 'GH', 'HG', 'HK', 'KH', 'KJ', 'JK', 'JA', 'AJ', 'BL', 'LB', 'CN', 'NC', 'EN', 'NE', 'NM', 'MN', 'ML', 'LM', 'FM', 'MF', 'AH', 'HA']


filename = current_datetime()+".csv"
with open(filename, 'a', newline='') as csvfile: 

    csvwriter = csv.writer(csvfile) 

    csvwriter.writerow(fields) 
        
    csvwriter.writerows(mainrows)


driver.quit()
