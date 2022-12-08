from diaries.DiarySample import DiarySample
from diaries.SasakiDiary import SasakiDiary
from diaries.FujiiDiary import FujiiDiary
from diaries.ShiraiDiary import ShiraiDiary

#
diaries = [
    DiarySample(), 
    FujiiDiary(), 
    SasakiDiary(),
    ShiraiDiary(),
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()