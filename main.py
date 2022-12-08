from diaries.DiarySample import DiarySample
from diaries.HidetoDiary import HidetoDiary
from diaries.SasakiDiary import SasakiDiary
from diaries.FujiiDiary import FujiiDiary

#
diaries = [
    DiarySample(), 
    HidetoDiary(),
    FujiiDiary(), 
    SasakiDiary(),
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()