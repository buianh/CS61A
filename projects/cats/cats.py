"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1
    my_lst = []
    for i in paragraphs:
        if select(i):
            my_lst.append(i)
    if k >= len(my_lst):
        return ''
    return my_lst[k]


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select(paragraph):
        nonlocal topic
        i = 0
        words = paragraph.lower().split()
        table = paragraph.maketrans('', '', string.punctuation)
        words = [w.translate(table) for w in words]
        while i < len(topic):
            if any([topic[i] == word for word in words]):
                return True
            i+=1
        return False
    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed) == 0 or len(reference) ==0:
        return 0.0
    else:
        typed_words = typed.split()
        ref_words = reference.split()
        count = 0
        for i in range(min(len(typed_words),len(ref_words))):
            if typed_words[i] == ref_words[i]:
                count+=1
            elif '\t'+typed_words[i] == ref_words[i]:
                count+=1
        return 100*(count/len(typed_words))
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed)*12/elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    my_lst = []
    for i in range(len(valid_words)):
        my_lst.append(diff_function(user_word,valid_words[i],limit))
    diff_index = my_lst.index(min(my_lst))
    #if sum([lst==min(my_lst) for lst in my_lst])==1:
    if user_word in valid_words:
        return user_word
    elif min(my_lst) <= limit:
        return valid_words[diff_index]
    return user_word
    #else:
        #new_lst =[]
        #for i in range(len(valid_words)):
            #bool_ind = (diff_function(user_word,valid_words[i],limit)==min(my_lst))
            #if bool_ind:
                #new_lst.append(valid_words[i])
        #def count_similar(typed_words,ref_words):
            #count = 0
            #for i in range(min(len(typed_words),len(ref_words))):
                #if typed_words[i] == ref_words[i]:
                    #count+=1
                #elif '\t'+typed_words[i] == ref_words[i]:
                    #count+=1
            #return count
       # new_lst1 = list(map(lambda x: count_similar(user_word,x),new_lst))
        #return new_lst[new_lst1.index(max(new_lst1))]
    # END PROBLEM 5


def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def similar(l1,l2):
        if l1==l2:
            return 0
        return 1
    if max(len(start),len(goal)) <= limit:
        if len(start)==len(goal)==1:
            return similar(start,goal)
        else:
            min_length=min(len(start),len(goal))
            return similar(start[0],goal[0])+ sphinx_swap(start[1:min_length], goal[1:min_length],limit) + abs(len(goal) - len(start))
    elif len(start) < 10 and len(goal)<10:
        if len(start)==len(goal)==1:
            return similar(start,goal)
        else:
            min_length=min(len(start),len(goal))
            return similar(start[0],goal[0])+ sphinx_swap(start[1:min_length], goal[1:min_length],limit) + abs(len(goal) - len(start))
    else: 
        #start_lst = iter(list(start))
        #goal_lst = iter(list(goal))
        #my_lst =[]
        #while i <= min(limit,len(start),len(goal)):
            #my_lst.append(similar(next(start_lst),next(goal_lst)))
            #i+=1
        #return sum(my_lst)+max(limit,len(start),len(goal))-min(limit,len(start),len(goal))
        if limit == 0 or limit==1:
            limit = min(len(start),len(goal))
        if len(start)==len(goal)==1:
            return similar(start,goal)
        min_length = min(limit,len(start),len(goal))
        return similar(start[0],goal[0])+ sphinx_swap(start[1:min_length], goal[1:min_length],limit) +max(limit,len(start),len(goal))-min(limit,len(start),len(goal))
        
    # END PROBLEM 6

#This solution does not pass all tests
def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    lst1 = list(start)
    lst2 = list(goal)
    def add(w1,w2):
        lst1=list(w1)
        lst2=list(w2)
        count_add = 0
        for i in range(min(len(lst1),len(lst2))-1):
            if lst1[i] == lst2[i+1] and lst1[i] != lst2[i]:
                lst1.insert(i,lst2[i])
                count_add +=1# Fill in the condition
        return lst1,lst2,count_add
    def add1(w1,w2):
        lst1=list(w1)
        lst2=list(w2)
        count_add = 0
        i=0
        while i < min(len(lst1),len(lst2)):
            if lst1[i] != lst2[i] and lst1[i-1]==lst1[i-1]:
                lst1.insert(i,lst2[i])
                count_add +=1
            i+=1
        return lst1,lst2,count_add
    def remove(w1,w2):
        lst1=list(w1)
        lst2=list(w2)
        count_remove = 0
        for i in range(1,min(len(lst1),len(lst2))):
            if lst1[i] == lst2[i-1] and lst1[i] != lst2[i]:
                lst1.pop(i-1)
                count_remove +=1# Fill in the condition
        return lst1,lst2,count_remove      
    add_diff = add(start,goal)  # Fill in these lines
    remove_diff = remove(start,goal) 
    add1_diff = add1(start,goal) 
    other_diff = sphinx_swap(start, goal, limit)
    if add_diff[2] == 1 and add_diff[1]==add_diff[0]:
        return add_diff[2]
    elif remove_diff[2] == 1 and remove_diff[1]==remove_diff[0]:
        return remove_diff[2]
    elif add1_diff[0] == add1_diff[1]:
        return add1_diff[2]
    if add_diff[2] == 0 and remove_diff[2]==0:
        return other_diff
    else:
        #substitute_diff = ... 
        # BEGIN
        "*** YOUR CODE HERE ***"
        return add_diff[2]+remove_diff[2]+ abs(len(start)-len(goal))


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def report_print(typed,prompt):
        i=0
        count = 0
        while i < min(len(typed),len(prompt)):
            if typed[i]==prompt[i]:
                count+=1
            else:
                i=100
            i+=1
        return count/len(prompt)
    progress = report_print(typed,prompt)
    report={'id':id,'progress':progress}
    send(report)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times =[]
    def diff(lst):
        result=[]
        for i in range(1,len(lst)):
            result.append(lst[i]-lst[i-1])
        return result
    for i in range(len(times_per_player)):
        times.append(diff(times_per_player[i]))
    return game(words,times)
    # END PROBLEM 9
    

def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    
    '''Create a min list'''
    my_lst_player = all_times(game)
    min_lst =  []
    result = [[] for _ in range(len(all_times(game)))]
    for i in range(len(all_words(game))):
        min_lst.append(min([player[i] for player in my_lst_player]))
    for i in range(len(all_times(game))):
        for j in range(len(all_words(game))):
            if my_lst_player[i][j]==min_lst[j]:
                result[i].append(all_words(game)[j])
    distinct_words = []
    distinct_words.extend(result[0])
    distinct_words
    for i in range(1,len(result)):
        word =list(set(result[i]) & set(distinct_words))
        for j in range(len(word)):
            result[i].remove(word[j])
        distinct_words.extend(result[i])
    return result
   
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)