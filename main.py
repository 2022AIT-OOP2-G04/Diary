from diaries.DiarySample import DiarySample
from diaries.ShiraiDiary import ShiraiDiary

#
diaries = [
    DiarySample(), 
    ShiraiDiary(),
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()