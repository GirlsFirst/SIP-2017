import turtle
import math

class User:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.connections = []

    def addConnection(self, connection_id):
        self.connections.append(connection_id)

    def getUserName(self):
        return self.user_name

    def getConnections(self):
        return self.connections

    def getUserID(self):
        return self.user_id

class Network:
    def __init__(self):
        self.users = []

    def numUsers(self):
        return len(self.users)

    def addUser(self, username):
        for user in self.users:
            if username == user.getUserName():
                print("Sorry, that name is taken. Try again.")
                return
        #If username wasn't taken, add user to the network
        user_id = len(self.users)
        self.users.append(User(username, user_id))


    def getUserID(self, username):
        user_id = -1
        for user in self.users:
            if username == user.getUserName():
                user_id = user.getUserID()
        return user_id                          #If user_id = -1, that means that the username is not there

    def addConnection(self, user1, user2):      #connections are both ways in this program
        user1_id = self.getUserID(user1)
        user2_id = self.getUserID(user2)

        user1 = self.users[user1_id]
        user2 = self.users[user2_id]

        if user1_id == -1 or user2_id == -1:
            print("Sorry, one or more username is not correct. Try again.")
            return False                           #Failure, one or other username is wrong
        elif user1_id == user2_id:
            print("Sorry, connections must be between two different users. Try again.")
            return False
        elif user2_id in user1.getConnections(): #They're already friends
            print("{} and {} are already connected!".format(user1.getUserName(), user2.getUserName()))
            return True
        else:
            self.users[user1_id].addConnection(user2_id)
            self.users[user2_id].addConnection(user1_id)
            return True                               #Success

    def printUsers(self):
        print("Network Users:")
        for user in self.users:
            print("\tUser {}: {}".format(user.getUserID(), user.getUserName()))

    def printConnections(self, username):
        user = self.users[self.getUserID(username)]
        connections = user.getConnections()
        print("{}'s connections:".format(user.getUserName()))
        for friendID in connections:
            friend = self.users[friendID]
            print("\t{}".format(friend.getUserName()))

def main():
    mynetwork = Network()
    done = False
    while not done:
        action = input("""\nWhat would you like to do?
            Add a user (u), print users (p),
            add connection (c), print connections (pc),
            quit (q)?
            """)

        if action == "p":
            mynetwork.printUsers()
        elif action == "u":
            username = input("What username? ")
            mynetwork.addUser(username)               
        elif action == "pc":
            user = input("For which user? ")
            mynetwork.printConnections(user)
        elif action == "c":
            if mynetwork.numUsers() < 2:
                print("You need at least two users to make a connection.")
                continue
            user1 = input("First username: ")
            user2 = input("Second username: ")
            mynetwork.addConnection(user1, user2)
        elif action == "q":
            print("Sorry to see you go so soon!")
            break
        else:
            print("Sorry, I didn't understand that.")

if __name__ == '__main__':
    main()
