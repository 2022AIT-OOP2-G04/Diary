from diaries.DiarySample import DiarySample
from diaries.K21036Diary import K21036Diary
from diaries.MasudaDiary import MasudaDiary
from diaries.HidetoDiary import HidetoDiary
from diaries.SasakiDiary import SasakiDiary
from diaries.FujiiDiary import FujiiDiary
from diaries.ShiraiDiary import ShiraiDiary
from diaries.AgataDiary import AgataDiary

#
diaries = [
    DiarySample(), 
    K21036Diary(), 
    MasudaDiary(),
    HidetoDiary(),
    FujiiDiary(), 
    SasakiDiary(),
    ShiraiDiary(),
    AgataDiary(), 
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
    
