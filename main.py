from diaries.DiarySample import DiarySample
from diaries.K21036Diary import K21036Diary

#
diaries = [
    DiarySample(), 
    K21036Diary(), 
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()