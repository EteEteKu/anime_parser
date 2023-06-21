class Anime:
    def __init__(self, name, typeanime, episode, status, poster, link):
        self.NAME = name
        self.TYPE = typeanime
        self.EPISODE = episode
        self.STATUS = status
        self.POSTER = poster
        self.LINK = link

    def get_all(self):
        all_info = {
            'name': self.NAME,
            'type': self.TYPE,
            'episode': self.EPISODE,
            'status': self.STATUS,
            'poster': self.POSTER,
            'link': self.LINK
        }
        return all_info