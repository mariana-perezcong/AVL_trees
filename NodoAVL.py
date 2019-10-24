__author__ = 'mperezcs'
class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def getKey(self):
        return self.key

    def __str__(self):
        return self.key
