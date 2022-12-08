from diaries.AbstractDiary import AbstractDiary

class AgataDiary(AbstractDiary):
    
    def get_date(self):
        return "2022-12-6"

    def get_summary(self):
        return "黒猫と出会った。猫を飼いたくなった。"

    def get_author(self):
        return "あがた"