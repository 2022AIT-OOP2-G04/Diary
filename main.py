from diaries.DiarySample import DiarySample
from diaries.HidetoDiary import HidetoDiary

#
diaries = [
    DiarySample(), 
    HidetoDiary(),
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()