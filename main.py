from diaries.DiarySample import DiarySample
from diaries.AgataDiary import AgataDiary

#
diaries = [
    DiarySample(),
    AgataDiary(), 
    ]

for d in diaries:
    print("---------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()