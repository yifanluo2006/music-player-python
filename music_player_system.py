from playlist import *
from song import *
from user import *

import numpy as np
import logging
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

class MusicPlayerSystem:
    def __init__(self):

        self.system_logger = logging.getLogger("system_logger")
        self.user_action_logger = logging.getLogger("user_action_logger")
        self.event_generation_logger = logging.getLogger("event_generation_logger")

        self.complete_list = Playlist("00000", "Complete Library", self) # initial playlist created
        self.populate_complete_list() # and populated

        self.system_logger.info("Welcome to the Music Player System by Yifan and Jaden!")

        self.first_user = None
        self.user = None

        for i in range(1, 101):
            self.import_user()
        self.system_logger.info("Total user count = " + str(self.get_user_num()))
        self.authenticated_user_id = None


    def populate_complete_list(self): # import the initial list with all songs
        file = open("./data/song_list.txt", "r") #reads the text file
        content = file.read()
        song_list = content.split('\n') #splits the entire elements of each song into a list, seperated by new line operator \n
        
        for song in song_list: # use this for loop to add songs into the list
            song_element = song.split('_')
            
            meta = [str(song_element[5]), str(song_element[6])]
            
            if len(song_element) == 8:
                meta.append(str(song_element[7]))
            elif len(song_element) == 9:
                meta.append(str(song_element[7]))
                meta.append(str(song_element[8]))
            elif len(song_element) == 10:
                meta.append(str(song_element[7]))
                meta.append(str(song_element[8]))
                meta.append(str(song_element[9]))
            
            self.complete_list.add_song(song_element[0], song_element[1], song_element[2], song_element[3], song_element[4], meta)
            self.system_logger.info(str(song_element[0]) + " " + str(song_element[1]) + " is loaded")
                
    def import_user(self):
        id = self.get_user_num() + 1
        if self.first_user is None:
            self.user = User(id, self.complete_list)
            self.first_user = self.user
        else:
            a_user = User(id, self.complete_list)
            self.user.set_next(a_user)
            self.user = a_user
            
    def add_user(self, name, password):
        id = self.get_user_num() + 1
        if self.first_user is None:
            self.user = User(id, self.complete_list, name, password)
            self.first_user = self.user
            self.system_logger.info("Total user count = " + str(self.get_user_num()))
        else:
            a_user = User(id, self.complete_list, name, password)
            self.get_last_user().set_next(a_user)
            self.user = a_user
            self.system_logger.info("Total user count = " + str(self.get_user_num()))
            
    def login_authentication(self, name, password):
        current_user = self.first_user
        while current_user is not None:
            if current_user.get_name() == name and current_user.get_password() == password:
                self.system_logger.info("AUTHENTICATION: User " + current_user.get_name() + " Has Authenticated")
                self.authenticated_user_id = current_user.get_id()
                return current_user
            current_user = current_user.get_next()
        
        return None

    def add_song_to_library(self, userId, songId):
        if self.get_user(userId) is not None and self.complete_list.search_song_id(songId) is not None:
            self.user = self.get_user(userId)
            self.user.add_song_to_library(songId, self.complete_list)
            if userId == self.authenticated_user_id:
                self.user_action_logger.info("Adding " + self.complete_list.search_song_id(songId).get_title() + " to user " + str(userId) + " " + str(self.get_user(userId).get_name()) + "'s library")
            else:
                self.event_generation_logger.info("Adding " + self.complete_list.search_song_id(songId).get_title() + " to user " + str(userId) + " " + str(self.get_user(userId).get_name()) + "'s library")

    def create_playlist(self, userId, playlistName):
        if self.get_user(userId) is not None:
            self.user = self.get_user(userId)
            self.user.add_playlist(playlistName)
            
        if userId == self.authenticated_user_id:
        
            self.user_action_logger.info("Playlist " + str(playlistName) + " added to user " + str(userId))
        else:
            self.event_generation_logger.info(("Playlist " + str(playlistName) + " added to user " + str(userId)))

    def add_song_to_playlist(self, userId, playlistId, songId):
        if self.get_user(userId) is not None and self.complete_list.search_song_id(songId) is not None:
            self.user = self.get_user(userId)
            self.user.add_song_to_playlist(playlistId, songId, self.complete_list)
            if userId == self.authenticated_user_id:
                self.user_action_logger.info("Adding " + self.complete_list.search_song_id(songId).get_title() + " to user " + str(userId) + " " + str(self.get_user(userId).get_name()) + "'s playlist")
            else:
                self.event_generation_logger.info("Adding " + self.complete_list.search_song_id(songId).get_title() + " to user " + str(userId) + " " + str(self.get_user(userId).get_name()) + "'s playlist")

    def delete_song_in_playlist(self, song, playlist):
        current_song = playlist.get_first_song()
        last_song = playlist.get_last_song()

        # If the song to be deleted is at the begining
        if current_song is not None and current_song.get_id() == song.get_id():
            playlist.set_first_song(playlist.get_first_song().get_next())
            if playlist.get_id()[3 : 5] == "00":
                self.complete_list.search_song_id(song.get_id()).update_frequency(-1)
                for new_playlist in playlist.get_owner().get_all_playlist():
                    self.delete_song_in_playlist(song, new_playlist)

            if playlist.get_owner().get_id() == self.authenticated_user_id:
                self.user_action_logger.info("Deleted " + song.get_title() + " from " + playlist.get_name())
            else:
                self.event_generation_logger.info("Deleted " + song.get_title() + " from " + playlist.get_name())
            return

        # If the song to be deleted is at the end
        if current_song is not None and last_song.get_id() == song.get_id():
            while current_song.get_next().get_next() is not None:
                current_song = current_song.get_next()
            current_song.set_next(None)
            playlist.reset_last_song()
            
            if playlist.get_owner().get_id() == self.authenticated_user_id:
                self.user_action_logger.info("Deleted " + song.get_title() + " from " + playlist.get_name())
            else:
                self.event_generation_logger.info("Deleted " + song.get_title() + " from " + playlist.get_name())
                
            if playlist.get_id()[3 : 5] == "00":
                self.complete_list.search_song_id(song.get_id()).update_frequency(-1)
                for playlist in playlist.get_owner().get_all_playlist():
                    self.delete_song_in_playlist(song, playlist)
        
        # If the song to be deleted is in the middle
        while current_song is not None and current_song.get_next() is not None:
            previous_song = current_song
            current_song = current_song.get_next()
            if current_song.get_id() == song.get_id():
                previous_song.set_next(current_song.get_next())
                
                if playlist.get_owner().get_id() == self.authenticated_user_id:
                    self.user_action_logger.info("Deleted " + song.get_title() + " from " + playlist.get_name())
                else:
                    self.event_generation_logger.info("Deleted " + song.get_title() + " from " + playlist.get_name())
                
                if playlist.get_id()[3 : 5] == "00":
                    self.complete_list.search_song_id(song.get_id()).update_frequency(-1)
                    for playlist in playlist.get_owner().get_all_playlist():
                        self.delete_song_in_playlist(song, playlist)

    """
    Advanced suggestion algorithm with weighted factors or ML concepts
    The core idea is collaborative filtering: we recommend songs to the current user based on users who have a similar preference in songs
    The functions I am using include the K-Nearest Neighbors Algorithm (k-NN) at its core to find the most similar users
    
    The steps I need to implement this is the following:
    1. Create a matrix with all users and all songs, with information on if the user owns the song or not
    2. Use cosine similarity to calculate how similar the user's tastes are for all users
    3. User k-NN algorithm to find the most similar user to the current user
    4. Find songs that the current user does not have in the similar user's library and recommend these songs
    """
    def generate_suggestions(self, userId, playlistId):
        if self.get_user(userId) is not None:
            # Since the assignment is based on linked-lists, the return will be the following linked-list
            suggested_songs = Playlist("99979", "Suggestions based on " + self.get_user(userId).get_playlist(int(playlistId[3 : 5])).get_name(), self)
            
            print("")
            if userId == self.authenticated_user_id:
                self.user_action_logger.info("Generating suggestions based on " + self.get_user(userId).get_playlist(int(playlistId[3 : 5])).get_name())
            else:
                self.event_generation_logger.info("Generating suggestions based on " + self.get_user(userId).get_playlist(int(playlistId[3 : 5])).get_name())
            
            "creates and populates matrix"
            # The idea for the following code was inspired by ChatGPT; however, the specific details are coded by myself
            # None of the following is copied and pasted
            user_num = self.get_user_num() + 1
            song_num = 1001 # note that in our case the 0 row and 0 column will always be empty, because there is no zero indicies. However, this is ok because we are never going to access these parts
            matrix = np.zeros((user_num, song_num), dtype=int)
            
            # This code to populate the matrix is entirely my design and code
            # I really like iterating through linked-lists with while loops, much better and safer than recursion
            current_user = self.first_user
            while current_user is not None:
                if current_user.get_id() != userId: # checking if the current user owns the target playlist, so we can have the playlist data instead of the user data in the matrix as the recommendation needs to be playlist specific
                    current_song = current_user.get_library().get_first_song()
                    while current_song is not None:
                        matrix[current_user.get_id(), current_song.get_numeric_id()] = 1
                        current_song = current_song.get_next()
                else:
                    current_song = current_user.get_playlist(int(playlistId[3:5])).get_first_song()
                    while current_song is not None:
                        matrix[current_user.get_id(), current_song.get_numeric_id()] = 1
                        current_song = current_song.get_next()
                    
                current_user = current_user.get_next()
            
            # np.set_printoptions(threshold=np.inf)
            # print(matrix)
            
            "calculate cosine similarity"
            # The following code is inspired by ChatGPT
            "User k-NN to find similar users"
            k = 21
            knn = NearestNeighbors(n_neighbors=k, metric='cosine')
            knn.fit(matrix)
            
            # I made modifications to the following:
            # According to the original code, only a user will be matched with a user, and there is no way to match playlists
            # To resolve this, I imported the playlist information for the when populating the target user, so even though it is called user, it is actually the information of a playlist
            target_user_index = userId # the target user id
            distances, indices = knn.kneighbors([matrix[target_user_index]])
            similar_users = indices.flatten()
            
            "find songs in similar users to give recommendations"
            # The following code is entirely my own:
            target_playlist = self.get_user(userId).get_playlist(int(playlistId[3:5]))
            
            user_index = 1
            while suggested_songs.get_len() <= 10 and user_index <= 20:
                similar_user = self.get_user(similar_users[user_index])
                
                # print(similar_users)
            
                current_song = similar_user.get_library().get_first_song()
                while current_song is not None:
                    if not target_playlist.is_duplicate(current_song.get_id()):
                        suggested_songs.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
                    current_song = current_song.get_next()
                user_index += 1
                if userId == self.authenticated_user_id:
                    self.user_action_logger.info("Matched preferences with user " + similar_user.get_name())
                else:
                    self.event_generation_logger.info("Matched preferences with user " + similar_user.get_name())

            if userId == self.authenticated_user_id:
                self.user_action_logger.info("Generated suggestions of matching songs")
            else:
                self.event_generation_logger.info("Generated suggestions of matching songs")
            print("")

            return suggested_songs

    """
    Sophisticated popularity tracking with trend analysis
    I will track the popularity with exponential moving average (EMA), which places a greater value on closer data points, thus indicating the trend
    Therefore, the formula will react to a trend faster than normal popularity tracking
    The idea of EMA was inspired by ChatGPT; however, the EMA part of code is entirely my own
    The formula and majority of calculations will be in song class
    Note that only the copy of the song within the complete list will be updated, all other copies in libraries and playlists will not as it is only nessecary to keep track of one record, and the complete list is the most accurate record
    """
    def get_most_popular_songs(self, n):
        popular_songs = Playlist("99989", "Top " + str(n) + " Trending Songs", self)

        current_song = self.complete_list.get_first_song()
        while current_song is not None:
            current_song.update_popularity() # updates popularity score for each song
            popular_songs.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta(), current_song.get_frequency(), current_song.get_popularity())
            current_song = current_song.get_next()

        print("")
        self.system_logger.info("Calculated popularity score by EMA")

        # To find the song with the highest popularity score as calculated, need to sort the linked-list
        # Merge sort is the most efficient
        # Original merge Sort code is partly from Geeks for Geeks, modified to sort by popularity and song objects, and also modified for OOP porgramming
        # The original code sorts in increasing order, I also modified it to sort in decreasing order

        popular_songs.set_first_song(self.merge_sort(popular_songs.get_first_song()))

        # return the most popular n songs
        popular_songs.slice(n)

        self.system_logger.info("Found top " + str(n) + " most trending songs ")
        print("")

        # most popular songs are returned in the format of a linked-list
        return popular_songs
    
    def split(self, head):
        if head is None or head.next is None:
            return None  # Cannot split further

        slow = head
        fast = head.next  # Start fast one node ahead

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None  # Split the list into two halves
        return second

    def merge(self, first, second):
  
        # If either list is empty, return the other list
        if not first:
            return second
        if not second:
            return first

        # Pick the smaller value between first and second nodes
        if first.popularity_score > second.popularity_score:
            first.next = self.merge(first.next, second)
            return first
        else:
            second.next = self.merge(first, second.next)
            return second

    def merge_sort(self, head):
  
        # Base case: if the list is empty or has only one node, 
        # it's already sorted
        if not head or not head.next:
            return head

        # Split the list into two halves
        second = self.split(head)

        # Recursively sort each half
        head = self.merge_sort(head)
        second = self.merge_sort(second)

        # Merge the two sorted halves
        return self.merge(head, second)

    """
    The fuzzy search algorithm is implemented in the Playlist class
    I did not use any libraries, instead, I have the code to calculate the levenshtein distance and similarity score
    I will use merge sort to sort the results and display the most relevant at the top
    """
    def search_songs_in_playlist(self, playlist, query):
        print("")
        self.system_logger.info("Searching for " + query + " in " + playlist.get_name())

        search_result = self.search_songs_title(playlist, query)
        search_result.append(self.search_songs_artist(playlist, query))
        search_result.append(self.search_songs_genre(playlist, query))
        search_result.append(self.search_songs_meta(playlist, query))

        # Merge sort the search result by similarity of result
        search_result.set_first_song(self.merge_sort_for_search(search_result.get_first_song()))
        self.system_logger.info("Found " + str(search_result.get_len()) + " search results!")
        print("")
        # The search function returns the result as a linked-list
        return search_result

    def search_songs_in_library(self, user, query): # searches in library
        search_result = self.search_songs_in_playlist(user.get_library(), query)
        return search_result

    def search_songs(self, query): # searches in complete list (entire collection)
        search_result = self.search_songs_in_playlist(self.complete_list, query)
        return search_result

    def search_songs_title(self, playlist, query): # searches by title, used by other search functions
        search_result = playlist.search_song_title(query)
        return search_result

    def search_songs_artist(self, playlist, query): # searches by artist, used by other search functions
        search_result = playlist.search_song_artist(query)
        return search_result

    def search_songs_genre(self, playlist, query): # searches by genre, used by other search functions
        search_result = playlist.search_song_genre(query)
        return search_result
    
    def search_songs_meta(self, playlist, query): #searches b meta tags, used by other search functions
        search_result = playlist.search_song_meta(query)
        return search_result
    
    def split_for_search(self, head):
        if head is None or head.next is None:
            return None  # Cannot split further

        slow = head
        fast = head.next  # Start fast one node ahead

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None  # Split the list into two halves
        return second

    def merge_for_search(self, first, second):
  
        # If either list is empty, return the other list
        if not first:
            return second
        if not second:
            return first

        # Pick the smaller value between first and second nodes
        if first.similarity > second.similarity:
            first.next = self.merge_for_search(first.next, second)
            return first
        else:
            second.next = self.merge_for_search(first, second.next)
            return second

    def merge_sort_for_search(self, head):
  
        # Base case: if the list is empty or has only one node, 
        # it's already sorted
        if not head or not head.next:
            return head

        # Split the list into two halves
        second = self.split_for_search(head)

        # Recursively sort each half
        head = self.merge_sort_for_search(head)
        second = self.merge_sort_for_search(second)

        # Merge the two sorted halves
        return self.merge_for_search(head, second)
    
    def save_changes_to_file(self):
        self.system_logger.info("Saving all changes to files")
        current_user = self.first_user

        while current_user is not None:
            file_name = "./data/user_" + str(current_user.get_id()) + ".txt"
            f = open(file_name, "w")

            f.write(str(current_user.get_id()) + "\n")
            f.write(str(current_user.get_name() + "\n"))
            f.write(str(current_user.get_password()) + "\n")

            playlists = current_user.get_all_playlist()
            f.write(str(len(playlists)) + "\n")

            for playlist in playlists:
                f.write(str(playlist.get_name()) + "\n")
                f.write(str(playlist.format_songs()) + "\n")

            self.system_logger.info("Saved changes to user" + str(current_user.get_id()) + " " + str(current_user.get_name()) + " to files")
            current_user = current_user.get_next()

        self.system_logger.info("Saved all changes to files")

    # ================= Accessor Methods =======================
    def get_user(self, id):
        current_user = self.first_user

        while current_user != None:
            if current_user.get_id() == int(id):
                return current_user
            else:
                current_user = current_user.get_next()

        return None

    def get_playlist(self, id):
        if int(id[0:3]) == 0:
            return self.complete_list
        else:
            self.user = self.get_user(int(id[0:3]))
            self.user.get_playlist(id)

    def get_user_num(self):
        num = 0
        user = self.first_user
        while user is not None:
            num+=1
            user = user.get_next()
            
        return num
    
    def get_last_user(self):
        
        user = self.first_user
        while user.get_next() is not None:
            user = user.get_next()
            
        return user
    
    def get_complete_list(self):
        return self.complete_list
        
    # =============== Testing ===============
    # def test_print(self):
    #     self.complete_list.print_list()