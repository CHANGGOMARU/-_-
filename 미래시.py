import time

jp_eve = 57
ko_eve = 0

eve_day_jp = 0
eve_day_kr = -9

day = 20
month = 5
year = 0



final_month = 0
final_day = 0
final_year = 0
while jp_eve > ko_eve:
    day = day + 1
    eve_day_jp = eve_day_jp + 1
    eve_day_kr = eve_day_kr + 1
    final_day = final_day + 1

    

    if day == 28 and month == 2:
        month = month+1
        day = 0
        
    if (day == 30) and (month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        day = 0
        month = month + 1
        
    if (day == 31) and (month == 4 or 6 or 9 or 11):
        day = 0
        month = month + 1
        
        
    
    if month == 13:
        year = year + 1
        month = 1
        
    


    if final_day == 28 and final_month == 2:
        final_month = final_month + 1
        day = 0
    if (final_day == 30) and (final_month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        final_day = 0
        final_month = final_month + 1
    elif (final_day == 31) and (final_month == 4 or 6 or 9 or 11):
        final_day = 0
        final_month = final_month + 1
    if final_month == 13:
        final_year = final_year + 1
        final_month = 1



    if eve_day_jp == 11:
        eve_day_jp = 0
        jp_eve = jp_eve + 1
    if eve_day_kr == 9:
        eve_day_kr = 0
        ko_eve = ko_eve + 1
        
    
    print ("일본    ",jp_eve,"   (",eve_day_jp,")   ","vs",ko_eve,"   (",eve_day_kr,")   ","    한국")
    print("현재날짜 : ",year, "년  ",month, "월  ",day, "일  ")




        
print ("총 이벤트수 : ",jp_eve,"개")
print("걸린시간 : ",final_year,"년  ",final_month,"개월  ",final_day,"일")
        
            
