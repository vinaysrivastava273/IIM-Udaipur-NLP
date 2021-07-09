# coding: utf-8
import random
import time
import requests
import json
import pprint
import ast
import openpyxl

domain = "https://graph.facebook.com/v9.0/"
my_insta_id = "YOUR_INSTAGRAM_ID"  # make sure you replace the instagram id with your own intagram id
part_A = "?fields=business_discovery.username("
part_B_List = []
media_after = "){media"
part_C = "{caption,media_type,like_count,comments_count,timestamp,media_product_type,paging,id,video_title}}&"
acces_token = "access_token=ACCESS_TOKEN"  # make sure you dont delete: access_token=

excel_file = openpyxl.load_workbook('Nifty50.xlsx')
sheet = excel_file['Sheet1']

global data

for i in range(3, 43):
    part_B_List.append(sheet.cell(row=i, column=4).value)

i=0
while i < len(part_B_List):

    file_name = part_B_List[i]+'.json'
    file = open(file_name, 'w')
    print(part_B_List[i])
    url = domain + my_insta_id + part_A + part_B_List[i] + media_after + part_C + acces_token
    data = requests.get(url)

    while True:
        
        results = ast.literal_eval(data.content.decode("UTF-8"))
        # print(data) # Success or not

        ig_data = results['business_discovery']['media']
        box = []
        j = 0

        while j < len(ig_data['data']):

            ig_post = ig_data['data'][j]

            if 'media_type' in ig_post:
                mtype = ig_post['media_type']
            else:
                mtype = ""

            likes = ig_post['like_count']
            comments = ig_post['comments_count']
            if 'caption' in ig_post:
                caption = ig_post['caption']
            else:
                caption = ""
            date = ig_post['timestamp']

            if 'media_product_type' in ig_post:
                ptype = ig_post['media_product_type']
            else:
                ptype = ""

            m_id = ig_post['id']

            if 'video_title' in ig_post:
                vtitle = ig_post['video_title']
            else:
                vtitle = ""

            box.append({"caption": caption, "media": mtype, "product_type": ptype, "likes": likes, "comments": comments, "DateOfPost": date, "IGTV Video Title": vtitle, "id": m_id})
            
            j += 1

        
        json.dump(box, file, indent=6)

        if 'paging' not in ig_data:
            break

        after_cursor = ig_data['paging']['cursors']
        if 'after' not in after_cursor:
            print (after_cursor)
            break

        new_url = domain + my_insta_id + part_A + part_B_List[0] + media_after + '.after(' + after_cursor['after'] + ')' + part_C + acces_token
        time.sleep(random.randint(2, 5))
        data = requests.get(new_url)
        
    i += 1

    file.close()
