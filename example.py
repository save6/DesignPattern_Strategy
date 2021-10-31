from abc import ABCMeta, abstractmethod
import random
import json


class Sorter(metaclass=ABCMeta):
    """ソートのインターフェース"""
    @abstractmethod
    def sort(self, musics):
        pass


class RandumSorter(Sorter):
    """ランダムにソートするクラス"""
    def sort(self, musics):
        """ランダムにソートするメソッド
        
        :param musics: 音楽のデータが入っているリスト
        :type musics: list(dict())
        """
        return random.sample(musics,len(musics))


class ArtistSorter(Sorter):
    """作者の名前でソートするクラス"""

    def sort(self, musics):
        """作者の名前でソートするメソッド
        
        :param musics: 音楽のデータが入っているリスト
        :type musics: list(dict())
        """
        return sorted(musics, key = lambda x: x["artist"])


class Exporter(metaclass=ABCMeta):
    """出力するインターフェース"""

    @abstractmethod
    def export(self, musics):
        pass


class JsonExporter(Exporter):
    """Json形式で出力するクラス"""

    def export(self, musics):
        """Json形式で出力するメソッド
        
        :param musics: 音楽のデータが入っているリスト
        :type musics: list(dict())
        """
        return json.dumps(musics)


class CsvExporter(Exporter):
    """CSV形式で出力するクラス"""

    def export(self, musics):
        """CSV形式で出力するメソッド
        
        :param musics: 音楽のデータが入っているリスト
        :type musics: list(dict())
        """
        return "\n".join([music["title"] + "," + music["artist"] for music in musics])


class MusicList:
    """Musicリストをソートと出力形式を指定して出力するクラス"""

    def __init__(self, sorter, exporter):
        self.exporter = exporter
        self.sorter = sorter
    
    def export(self, musics):
        """Musicリストをソートと出力形式を指定して出力するメソッド
        
        :param musics: 音楽のデータが入っているリスト
        :type musics: list(dict())
        """
        SORTED = self.sorter.sort(musics)
        return self.exporter.export(SORTED)

DATA = [
    {"title": "ズルい女", "artist": "シャ乱Q"},
    {"title": "ロビンソン", "artist": "スピッツ"},
    {"title": "愛の言霊", "artist": "サザンオールスターズ"},
    {"title": "みんなのうた", "artist": "サザンオールスターズ"},
]

#SORTER = ArtistSorter()
SORTER = RandumSorter()
#EXPORTER = JsonExporter()
EXPORTER = CsvExporter()
MUSIC_LIST = MusicList(SORTER, EXPORTER)
print(MUSIC_LIST.export(DATA))
