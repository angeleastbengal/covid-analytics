#---------------------------------Student ID: 31131867---------------------------------------
#---------------------------------Name: Angel Das--------------------------------------------
#---------------------------------Create Date: 05-06-2020------------------------------------
#---------------------------------Last Modified: 07-06-2020----------------------------------
#---------------------------------Note: Version Control is used to save files----------------

class Person:

    #-------------------------Declaring a global variable to keep track of unique objects-------------------------------
    #-------------------------Note: This list is used to keep a check that only one object per person exists-----------------
    """
    The global object ensures that if there is a scenario where a person has multiple friends, but not all
    friends are present as a Person, in such scenarios unique objects are created for every record in the dataset.
    """

    global all_person_object
    all_person_object=[]

    """
    CONSTRUCTOR:
    Constructor: To initialize the class variables. Note only first and last name is passed into the constructor.
    The list to store friends/connections is initialized here.
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reference_friends=[]
        self.name=first_name+" "+last_name #----------created to store complete name of the Person
        """
        Each person object must be able to store a set of references to other Person objects.
        Hence every object is assigned a list to store their list of friends.
        """

    """
    FUNCTION DEFINITION:
    add_friend is utilized to store a set of reference to other person objects.
    """

    def add_friend(self, friend_person):
        self.reference_friends.append(friend_person)

    """
    FUNCTION DEFINITION:
    get_name is utilized to return the first and last name of an object.
    """

    def get_name(self):
        return self.name

    """
    FUNCTION DEFINITION:
    get_friends returns a list of Person objects for the social connections that have been created.
    """

    def get_friends(self):
        return self.reference_friends

    """
    FUNCTION DEFINITION:
    check_exist_name is used to find if a first_name and last_name is already added as an object. If yes
    the function returns 1 else -1. This utilized to ensure that each patient is represented as one unique
    object within the simulation. New patient objects are not created each time a friend is added if the friend exists.
    """
    def check_exists_name(self, f_name,l_name):

        if len(all_person_object)==0:
            return -1
        else:
            for object in all_person_object:
                name_present=object.first_name+object.last_name
                if name_present==(f_name+l_name):
                    return 1

        return -1

    """
    FUNCTION DEFINITION:
    return_object_name returns the object address if a particular name was already added to the list.
    """

    def return_object_name(self,f_name,l_name):

        for object in all_person_object:
            name_present = object.first_name + object.last_name
            if name_present == (f_name + l_name):
                return object




def load_people():
    #---------------------Variables to store the first and last name-----------------------
    first_name = ""
    last_name = ""
    global all_person_object
    all_person_object = []

    #--------------------List: To store the list of all Person objects that have been created from the file records----
    list_person_obj=[]
    list=[]

    # ----------------------------Reading data from a file-------------------------------------
    # ----------------------------Please note that file is stored in the same location as that of the project-------
    file_data = open("a2_sample_set.txt", "r")

    obj_count = 0  # -----------------count Person object for each record line-------------------
    friend_count = 0  # --------------count friends added for each object------------------------
    all_person_object_cnt = 0  # ----------Count total objects added-----------------------------

    for line in file_data:
        count_words = 1 #-------------Every name should have first and last name

        """
        count_words is used as a counter variable to identify if the work extracted is the last name or not.
        E.g. for Angel Das, the counter will be even when we read "Das" from the file. This will be used as an indicator
        to create the object or identify the end of a person's name (last name);
        """

        for word in line.split():

            # print(word, count_words)
            if count_words % 2 == 1:
                first_name = word

            else:
                if (word[len(word) - 1] == ',') or (word[len(word) - 1] == ':'):
                    word = word[0:len(word) - 1] #-------------removing the separator from the word
                last_name = word

                # print(first_name, " ", last_name)


            # print(first_name, last_name)
            #-----------------------Need to check if a name already exists in the list or not---------------------------

            if count_words%2==0:
                Dummy_obj=Person('A','B')
                boln=Dummy_obj.check_exists_name(first_name,last_name)


                if boln==-1:

                    # print(boln)
                    #-----------------------Creating a new person object for each record line-------------------------------
                    if count_words==2:
                        list_person_obj.append(Person(first_name,last_name)) #----------Creating the Person object
                        all_person_object.append(list_person_obj[obj_count]) #----------Storing it in a global variable
                        all_person_object_cnt+=1
                        obj_count += 1
                        # print("Person:",first_name, last_name)


                    #----------------------Adding friend of that object-----------------------------------------------------
                    elif count_words%2==0:

                        all_person_object.append(Person(first_name,last_name))
                        list_person_obj[obj_count-1].add_friend(all_person_object[all_person_object_cnt])
                        # print(all_person_object[all_person_object_cnt].first_name)
                        all_person_object_cnt += 1
                        # print("Friend:", first_name, last_name)


                else:
                    # print(boln)
                    # print("-----------------------------------------")
                    temp=Dummy_obj.return_object_name(first_name,last_name)
                    # -----------------------Creating a new person object for each record line------------------------------
                    if count_words == 2:
                        list_person_obj.append(temp)  # ----------Creating the Person object
                        obj_count += 1
                        # all_person_object.append(temp)  # ----------Storing it in a global variable
                        # all_person_object_cnt += 1
                        # print("Person:", temp.first_name, temp.last_name)

                    elif count_words % 2 == 0:
                        list_person_obj[obj_count-1].add_friend(temp)
                        # print("Friend:", temp.first_name, temp.last_name)



            count_words += 1


    file_data.close()
    return list_person_obj


if __name__ == '__main__':

    list_of_person=load_people()
    print(len(list_of_person))
    print(type(list_of_person))
    print("------------------------------Person Object-------------------------------")
    for object in list_of_person:
        print(object.get_name()+"------------------------------------------------")
        print("#friends:",len(object.get_friends()))
        for ob in object.reference_friends:
            print(ob.get_name())




