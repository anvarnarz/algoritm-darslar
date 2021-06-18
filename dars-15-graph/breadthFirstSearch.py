from collections import deque


def search(start_node, target='elon musk'):
    search_queue = deque()
    search_queue += graph[start_node]  
    searched = set()
    
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f'{target}ni topdik!')
                # print(searched)
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False



if __name__ == '__main__':

    graph = {'siz': ['ali', 'vali', 'tohir'],
             'ali': ['aziza', 'olim'],
             'vali': ['botir', 'ziyoda'],
             'tohir': ['elon musk', 'mohir'],
             'olim': [],
             'aziza': [],
             'botir': [],
             'ziyoda': ['aziza'],
             'elon musk': [],
             'mohir': []
             }












    print(search('siz'))
    print(search('ali','vali'))
