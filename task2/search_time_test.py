import time
import random
from linkedbst import LinkedBST


def read_from_file(filename):
    '''
    Reads the dictionary from a file named filename
    :param filename: str
    :return: None
    '''
    inf = []
    file = open(filename, "r", encoding="utf8")
    data = file.read().split("\n")
    for exp in data:
        if exp:
            if exp[0].isalpha():
                inf.append(exp.split()[0])
    file.close()
    return inf


def search_in_list(words, randomed):
    '''
    Searches 10 000 random chosen words in the dictionary using built-in list collection.
    :param words: list
    :param randomed: randomised list
    :return:int
    '''
    start = time.time()
    for el in randomed:
        words.index(el)
    end = time.time()
    return end - start


def search_in_bst(words, randomed):
    '''
    Searches 10 000 random chosen words in the dictionary using LinkedBST.
    :param words:list
    :param randomed:randomised list
    :return:int
    '''
    random.shuffle(words)
    tree = LinkedBST(words)
    start = time.time()
    for el in randomed:
        tree.find(el)
    end = time.time()
    return end - start


def search_in_balanced_bst(words, randomed):
    '''
    Searches 10 000 random chosen words in the dictionary using balanced LinkedBST.
    :param words:list
    :param randomed:randomised list
    :return:int
    '''
    tree = LinkedBST(words)
    tree.rebalance()
    start = time.time()
    for el in randomed:
        if tree.find(el):
            continue
    end = time.time()
    return end - start

words = read_from_file("words.txt")
randomed = random.choices(words, k=10000)
print(search_in_list(words, randomed))
print(search_in_bst(words, randomed))
print(search_in_balanced_bst(words, randomed))
