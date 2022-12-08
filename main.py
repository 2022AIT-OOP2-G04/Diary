from diaries.DiarySample import DiarySample
from diaries.ShiraiDiary import K21067Diary

#
diaries = [
    DiarySample(), 
    K21067Diary(),
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()