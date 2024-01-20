import random


class RandomizedSet:
    def __init__(self):
        self.storeSet = {}
        self.storeList = []

    def insert(self, val: int) -> bool:
        if val in self.storeSet:
            return False
        else:
            self.storeList.append(val)
            self.storeSet[val] = len(self.storeList) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.storeSet:
            index = self.storeSet[val]
            zero_val = self.storeList[-1]
            self.storeSet[zero_val] = index
            self.storeList[index], self.storeList[-1] = (
                self.storeList[-1],
                self.storeList[index],
            )
            self.storeList.pop()
            self.storeSet.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.storeList)
