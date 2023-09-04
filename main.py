from pprint import pprint as pp
from parser_func import parser_regions, parser, get_regions_index_choose
import multiprocessing
from multiprocessing import freeze_support
import time
from json_func import data_frame_into_json
import pandas as pd
main_link = 'https://baza-gai.com.ua'




def get_regions(index:int):
    main_object = parser_regions()
    region = main_object.find_all('tbody')
    region = region[0].find_all('td', class_="table-active")
    region = region[index]
    region_link = region.find('a')['href']
    region_link = f'{main_link}{region_link}'

    return region_link


def get_number_combination_start(region:str, start_from:int, count:int = 1):
    region_pars = parser(region)
    region_pars = region_pars.find_all('ul', class_="list columns-9 mb-3")
    
    link_arr = []
    for i in range(count, len(region_pars)):
        data = region_pars[i]
        data = data.find_all('a')
            
        for j in data:
            check_num = j.text[2:-2]
            if int(check_num) >= start_from:
                part = j['href']
                link = f'{main_link}/regions/{part}'
                link_arr.append(link)
            else:
                continue
    
    return link_arr          
        
    
def get_number_combination_medium(arr:list):
    data_set = []
    for i in arr:
        data = parser(i)
        data = data.find_all('ul', class_="list")
        data = data[0].find_all('li')
        link_update = i[:-4]
        for j in data:
            link = j
            link = link.find_all('a')
            link = link[0]['href']
            first_part_number = link
            link = f'{link_update}{link}'

            element = (link, first_part_number)
            data_set.append(element)
            
    return data_set
                          

def get_number_multy(element):
    main_object = parser(element[0])
    part = main_object.find_all('p')
    part = part[0].text
    part = part.split()
    part = int(part[2])

    if part == 0:
        return
    
    else:
        num_end = main_object.find_all('ul')
        num_end = num_end[1].find_all('a')
        arr = []
        for k in num_end:
            number = f'{element[1]}{k.text}'
            print(number)
            arr.append(number)
        
        dataframe_number = pd.DataFrame({'Number': arr})
        
        return dataframe_number

       
def process(arr:list):
    pool = multiprocessing.Pool(multiprocessing.cpu_count()*2)
    data = pool.map(get_number_multy, arr)
    
    # for i in data:
    #     combined_df = pd.concat([data[0], i], ignore_index=True)
    
    combined_df = pd.concat(data, ignore_index=True)
    
    return combined_df
    

    
def main():
    choose_region_arr = [
    "г. Киев",
    "Киевская область",
    "Винницкая область",
    "Волынская область",
    "Днепропетровская область",
    "АР Крым",
    "Донецкая область",
    "Житомирская область",
    "Закарпатская область",
    "Запорожская область",
    "Ивано-Франковская область",
    "Кировоградская область",
    "Луганская область",
    "Львовская область",
    "Николаевская область",
    "Одесская область",
    "Полтавская область",
    "Ровенская область",
    "Севастополь",
    "Сумская область",
    "Тернопольская область",
    "Харьковская область",
    "Херсонская область",
    "Хмельницкая область",
    "Черкасская область",
    "Черниговская область",
    "Черновицкая область"	
    ]
    
    for index, region in enumerate(choose_region_arr):
        print(index, region)
    
    print('Choose region which you want to parse')
    region_choose = int(input('Choose: '))
    
    print('Choose first 2 number "from 00 to 99" which you want to parse')
    first_num_parse_choose = int(input('Choose: '))
    
    
    region_index_choose = get_regions_index_choose(region_choose)
    print('Choose region id "from 1 upto 4" from what region whould start parsering\nexample:')
    for index, region in enumerate(region_index_choose[::-1]):
        print(f'{region}: {index+1}')
    
    region_id_choose = int(input('Choose: '))
    
    print('Choose dir to save file (.json)')
    path_choose = str(input('Choose: '))
    
    
    start = time.time()
    
    print('get region')
    a1 = get_regions(region_choose)
    

    print('get number start')
    b1 = get_number_combination_start(a1, first_num_parse_choose, count=region_id_choose)

    print('get number medium')
    c1 = get_number_combination_medium(b1)
    
    
    print('get_number')
    d1 = process(c1)
    pp(d1)
    

    print('data frame to json')
    e1 = d1.to_json(orient='records', indent=4)
    
    data_frame_into_json(path_choose, e1)
    end = time.time() - start
    print(f'{end/60} min')
    
    

if __name__ == '__main__':
    main()