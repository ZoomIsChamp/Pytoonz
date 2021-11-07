# CA 1      pytoonz.py
# Odhran Sexton     119361266

class DLLNode:

    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode

    def __str__(self):
        return "%s" % self.element


class Track:

    def __init__(self, name, artiste, timesplayed):
        self.name = name
        self.artiste = artiste
        self.timesplayed = timesplayed

    def __str__(self):
        return "%s; %s (%d)" % (self.name, self.artiste, self.timesplayed)

    def get_name(self):
        return self.name

    def get_artiste(self):
        return self.artiste

    def play(self):
        self.timesplayed += 1


class PyToonz:

    def __init__(self):
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(None, self.head, None)
        self.head.next = self.tail
        self.size = 0
        self.cursor = None

    def __str__(self):
        playlist = "Playlist: \n"
        song = self.head.next
        i = 0
        while i < self.size:
            if self.cursor == song:
                playlist += "--> %s\n" % song
                song = song.next
            else:
                playlist += "%s \n" % song
                song = song.next
            i += 1
        return playlist

    def length(self):
        return self.size

    def add_track(self, track):
        new_track = DLLNode(track, None, None)
        if self.size == 0:
            self.head.next = new_track
            self.cursor = self.head.next
        new_track.prev = self.tail.prev
        new_track.next = self.tail
        new_track.prev.next = new_track
        self.tail.prev = new_track
        self.size += 1

    def get_current(self):
        if self.size == 0:
            return None
        return "Current track: %s \n" % self.cursor

    def add_after(self, track):
        if isinstance(track, DLLNode):
            track.next = self.cursor.next
            track.prev = self.cursor
            self.cursor.next = track
            self.size += 1
        else:
            new_track = DLLNode(track, None, None)
            new_track.next = self.cursor.next
            new_track.prev = self.cursor
            self.cursor.next = new_track
            self.size += 1

    def next_track(self):
        if self.cursor.next == self.tail:
            self.cursor = self.head.next
        else:
            self.cursor = self.cursor.next

    def prev_track(self):
        if self.cursor.prev == self.head:
            self.cursor = self.tail.prev
        else:
            self.cursor = self.cursor.prev

    def reset(self):
        self.cursor = self.head.next

    def play(self):
        if self.cursor:
            self.cursor.element.play()
            print("Playing: %s \n" % self.cursor.element)
        else:
            print("There is no currently selected track")

    def remove_current(self):
        self.cursor.prev.next = self.cursor.next
        self.cursor.next.prev = self.cursor.prev
        self.size -= 1
        if self.cursor.next == self.tail:
            self.cursor.next = None
            self.cursor.prev = None
            self.cursor = self.head.next
        else:
            self.cursor = self.cursor.next
