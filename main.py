
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC



spisok_day={'29.08.2022':'1','12.09.2022':' 3-4 неделя 12.09.2022-25.09.2022','26.09.2022':' 5-6 неделя 26.09.2022-09.10.2022','10.10.2022': "7-8 неделя 10.10.2022-23.10.2022",'24.10.2022':" 9-10 неделя 24.10.2022-06.11.2022"}
spisok=({8:"ЕНИ",11:"Институт интегрированных форм обучения",9:"Институт международного сотрудничества",4:"Институт транспортного строительства",1:"Институт тяги и подвижного состава",2:"Институт управления, автоматизации и телекоммуникаций",3:"Институт экономики",
        34:"Российско-китайский транспортный институт",7:"Социально-гуманитарный институт",5:"Факультет воздушных сообщений",6:"Электроэнергетический институт"
            })
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
url = "https://dvgups.ru/index.php?Itemid=10000&option=com_timetable&view=newtimetable"
driver.get(url)
a = driver.find_elements(By.NAME, 'facultet')
a1 = Select(driver.find_element(By.NAME, 'facultet'))
groups = []
wait = WebDriverWait(driver, 10)
visible_element = Select(wait.until(EC.visibility_of_element_located((By.ID, "facultet"))))
visible_group = Select(wait.until(EC.visibility_of_element_located((By.ID, "group"))))
visible_time = Select(wait.until(EC.visibility_of_element_located((By.ID, "time"))))
# values_time = "29.08.2022"
for key, value in spisok.items():
        print(key, value)
values = input()
visible_element.select_by_value(values)
# visible_time.select_by_value(values_time)
time.sleep(4)
visible_element1 = wait.until(EC.visibility_of_element_located((By.ID, "group")))
select = Select(wait.until(EC.visibility_of_element_located((By.ID, "group"))))
groups.append(visible_element1.text.splitlines())

d = 0
keys = []
a = []
for i in groups:
        for s in i:
                d += 1
                keys.append(f"{s}")
keys = keys[1:]
the_dict = {x: keys[x] for x in range(d - 1)}
for key, value in the_dict.items():
        print(key, value)

select_group = int(input())
s = the_dict[select_group].replace("'", '"')
print(s)
select.select_by_visible_text(s)


PARA = []

time.sleep(4)
df = driver.find_elements(By.CLASS_NAME, 'table')
for i in df:

        s = i.find_elements(By.CLASS_NAME, 'col-2')

        s1 = i.find_elements(By.CLASS_NAME, 'd-flex')
        PRIPOT = []
        for i in s1:

                p1 = (i.find_element(By.CLASS_NAME, 'col-2').text)
                p2 = (i.find_element(By.CLASS_NAME, 'col-4').text)
                p3 = (i.find_element(By.CLASS_NAME, 'col-sm-2').text)
                PRIPOT += [(f'{p1}' , f'{p2}',f'{p3}')]
                PARA.append(PRIPOT)
        print(PRIPOT)
print(PARA)




time.sleep(4333)






