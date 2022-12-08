from diaries.DiarySample import DiarySample
from diaries.FujiiDiary import FujiiDiary

#
diaries = [
    DiarySample(),
    FujiiDiary(), 
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()