#---------------------------------Student ID: 31131867---------------------------------------
#---------------------------------Name: Angel Das--------------------------------------------
#---------------------------------Create Date: 05-06-2020------------------------------------
#---------------------------------Last Modified: 07-06-2020----------------------------------
#---------------------------------Note: Version Control is used to save files----------------

from a2_31131867_task1 import *
import random
import sys as sy
import math



class Patient(Person):
    # -------------------------Declaring a global variable to keep track of unique objects-------------------------------
    # -------------------------Note: This list is used to keep a check that one object per patient exists-----------------
    global all_patient_object
    all_patient_object = []

    """
    CONSTRUCTOR:
    Constructor: To initialize the class variables. It creates a Patient object by inheriting from the Person Class.
    Note only first, last name, and health 
    are passed to the constructor. The list to store friends/connections is initialized here.
    """

    def __init__(self, first_name, last_name, health):
        # self.first_name = first_name
        # self.last_name = last_name
        # self.reference_friends = []
        super().__init__(first_name,last_name)
        self.health=health

    """
    FUNCTION DEFINITION:
    The method returns the patients current health points.
    """

    def get_health(self):
        return self.health

    """
    FUNCTION DEFINITION:
    The method changes the patient's current health point directly.
    """

    def set_health(self, new_health):

        if new_health<0:
            new_health=0
        elif new_health>100:
            new_health=100

        self.health=new_health

    """
    FUNCTION DEFINITION:
     The method returns a boolean value based on the patient's current health points. If a patient's health point is in 
     range of 100 to 50, it returns False, i.e. the patient is not contagious else returns True. Note: Multiple if-elif
     is used to keep the structure of contagious check similar to the assignment specification.
    """

    def is_contagious(self):
        #----------Patient's health is rounded to the nearest integer to check for contagious scenarios
        health_score=round(self.get_health(),0)

        if (health_score>=76) and (health_score<=100):
            return False
        elif health_score==75:
            return False
        elif health_score>=50 and health_score<=74:
            return False
        elif health_score>=30 and health_score<=49:
            return True
        else:
            return True

    """
    FUNCTION DEFINITION:
    The method infects the patient object with a viral load. It causes the patient to receive the viral load specified 
    in the method's argument. Below pointers illustrates a few characteristics of the function and its
    attributes:
    1. viral_load is a floating-point number
    2. viral_load is usually subtracted from the Patient's health, hence health won't go beyond 100
    3. The health of a patient can fall below 0 after the viral load is subtracted hence, 
       such exceptions are handled in the function below      
    """

    def infect(self, viral_load):
        health_score=self.get_health()
        new_hp=0

        if health_score<=29:
            new_hp=health_score-0.1*viral_load
        elif health_score>29 and health_score<50:
            new_hp = health_score - 1 * viral_load
        else:
            new_hp = health_score - 2 * viral_load

        #-----------------------Health Points can't be less than 0, so after adding a viral load it falls below 0
        #-----------------------We adjust it to zero-------------------------------------------------------------
        #------------------After adding a viral load, health points can't be >100, hence the condition is not checked--
        if new_hp<0:
            new_hp=0

        self.health=new_hp

    """
    FUNCTION DEFINITION:
    This method allows the patient to recover some health points. If the health of the patient after the addition 
    of 5 health points exceeds beyond 100, then the health is reset to 100 else 5 extra health points gets added.
    """

    def sleep(self):

        health_score=self.health+5 #-----------Calculating health score of a patient
        if health_score>=100:
            self.health=100
        else:
            self.health=health_score

    """
    FUNCTION DEFINITION:
    check_exist_name is used to find if a first_name and last_name is already added as an object. If yes
    the function returns 1 else -1. This utilized to ensure that each patient is represented as one unique
    object within the simulation. New patient objects are not created each time a friend is added if the friend exists.
    """

    def check_exists_pat(self, f_name, l_name):

        if len(all_patient_object) == 0:
            return -1
        else:
            for object in all_patient_object:
                name_present = object.first_name + object.last_name
                if name_present == (f_name + l_name):
                    return 1

        return -1

    """
    FUNCTION DEFINITION:
    return_object_name returns the object address if a particular name was already added to the list.
    """

    def return_object_pat(self, f_name, l_name):

        for object in all_patient_object:
            name_present = object.first_name + object.last_name
            if name_present == (f_name + l_name):
                return object

"""
FUNCTION DEFINITION:
This function takes in days, meeeting_probability, and health of the first patient as input and simulates
the number of patients impacted each day. The end output of this function is a list containing the count of the affected
person for the number of days specified.

Assumptions:
1. The order of which Patient is simulated first for calculating the spread of a disease and the consecutive ones
are randomized using the concept of a random sample
"""


def run_simulation(days, meeting_probability, patient_zero_health):
    global all_patient_object
    all_patient_object=[]
    #----------------------------Exception handling-----------------------------------------------------
    #----------------------------A Patient's health should always lie between 0 and 100------------------
    #----------------------------Meeting probabilities should lie between o and 1------------------------

    if patient_zero_health<0:
        patient_zero_health=0
    elif patient_zero_health>100:
        patient_zero_health=100

    if meeting_probability < 0 or meeting_probability>100:
        sy.exit('Can\'t simulate as probability scores are incorrect')

    #-------------------------Calling function load_patients to read the patient and friend objects and assign
    #-------------------------them with their initial health-----------------------------------------------------------

    list_pat=load_patients(patient_zero_health)

    # for ob in list_pat:
    #     print(ob.get_name())
    #     print(ob.get_health())



    viral_load = 0 #--------------------------Variable to store viral load of each patient
    list_contagious=[] #----------------------List to keep count of contagious patients-------------------------




    #---------------Simulating days----------------------------------------------------------------
    for i in range(0,days):

        counter_random_meet=0
        list_random=[]
        # ---------------The meeting needs to be randomized, hence for evey day a random set of indexs are generated----
        # ---------------This index is used to determine which patient starts their journey-------------
        # list_random = random.sample(range(0, len(list_pat)), len(list_pat))
        list_random.extend(range(0, len(list_pat)))
        #------Loop simulatie impact on all patient objects----------------
        for y in range(0,len(list_pat)):


            obj=list_pat[list_random[counter_random_meet]] #-----------Selecting Random Patient to start the simulation
            health_score=obj.get_health()
            counter_random_meet+=1

            if obj.is_contagious()==True:
                 # print(obj.get_name())
                 viral_load=5+((health_score-25)**2)/62 #------------------Calculating Viral Load--------------------
            else:
                viral_load=0

            #------------For every friend a patient can visit, checking if they are infected--------------------------

            for ob in obj.reference_friends:
                rand=random.random()
                viral_l_frnd=0

                if rand<=meeting_probability:

                    if ob.is_contagious()==True: #------------------Checking if the friend is contagious or not
                        viral_l_frnd = 5 + ((ob.get_health() - 25) ** 2) / 62

                    ob.infect(viral_load)
                    obj.infect(viral_l_frnd)



        #----------------Checking patients contagious in the simulation------------------------
        #----------------Assumption: All friends are present as Patient objects as well--------
        count = 0
        for pat_object in list_pat:

            # print(pat_object.first_name,"-",pat_object.health)
            if pat_object.is_contagious()==True:
                count+=1

        list_contagious.append(count)


        #-----------------------Every Patient Object is rested to recover some health points by end of the day---------
        for pat_object in list_pat:
            pat_object.sleep()

    return list_contagious





def load_patients(initial_health):
    # ---------------------Variables to store the first and last name-----------------------
    first_name = ""
    last_name = ""
    # all_patient_object=[]

    # ------------------List: To store the list of all patient objects that have been created from the file records----
    list_patient_obj = []
    list = []

    # ----------------------------Reading data from a file-------------------------------------
    # ----------------------------Please note that file is stored in the same location as that of the project-------
    file_data = open("a2_sample_set.txt", "r")

    obj_count = 0  # -----------------count patient object for each record line-------------------
    friend_count = 0  # --------------count friends added for each object------------------------
    all_patient_object_cnt = 0  # ----------Count total objects added-----------------------------

    for line in file_data:
        count_words = 1  # -------------Every name should have first and last name

        """
        count_words is used as a counter variable to identify if the work extracted is the last name or not.
        E.g. for Angel Das, the counter will be even when we read "Das" from the file. This will be used as an indicator
        to create the object or end of a person's name;
        """

        for word in line.split():

            # print(word, count_words)
            if count_words % 2 == 1:
                first_name = word

            else:
                if (word[len(word) - 1] == ',') or (word[len(word) - 1] == ':'):
                    word = word[0:len(word) - 1]  # -------------removing the separator from the word
                last_name = word

                # print(first_name, " ", last_name)

            # print(first_name, last_name)
            # -----------------------Need to check if a name already exists in the list or not--------------------------

            if count_words % 2 == 0:
                #------------------Dummy object is created to keep a record of all patient objects----------------------
                Dummy_obj = Patient('A', 'B',0)

                #----------------Checking if object for a patient already exists----------------------------------------
                boln = Dummy_obj.check_exists_pat(first_name, last_name)

                if boln == -1:

                    # print(boln)
                    # -----------------------Creating a new patient object for each record line-------------------------
                    if count_words == 2:

                        list_patient_obj.append(Patient(first_name, last_name,initial_health))
                        initial_health=75 #-----for remaining patients health should be assigned to 75

                        # ----------Creating the patient object

                        all_patient_object.append(list_patient_obj[obj_count])  # ----------Storing it in a global variable
                        all_patient_object_cnt += 1
                        obj_count += 1



                    # ----------------------Adding friend of that object------------------------------------------------
                    elif count_words % 2 == 0:

                        all_patient_object.append(Patient(first_name, last_name,initial_health))
                        list_patient_obj[obj_count - 1].add_friend(all_patient_object[all_patient_object_cnt])

                        all_patient_object_cnt += 1


                #----------------------------If object already exists, adding the object address------------------------
                else:
                    # print(boln)
                    # print("-----------------------------------------")

                    temp = Dummy_obj.return_object_pat(first_name, last_name)
                    # -----------------------Creating a new person object for each record line--------------------------
                    if count_words == 2:
                        list_patient_obj.append(temp)  # ----------Creating the Person object
                        obj_count += 1
                        # all_person_object.append(temp)  # ----------Storing it in a global variable
                        # all_person_object_cnt += 1
                        # print("Person:", temp.first_name, temp.last_name)

                    elif count_words % 2 == 0:
                        list_patient_obj[obj_count - 1].add_friend(temp)
                        # print("Friend:", temp.first_name, temp.last_name)

            count_words += 1

    file_data.close()
    return list_patient_obj


if __name__ == '__main__':

    # list_of_patient = load_patients(49)
    # print(len(list_of_patient))
    # print(type(list_of_patient))
    # print("------------------------------Person Object-------------------------------")
    # for object in list_of_patient:
    #     print(object.get_name() ,"-",str(object.get_health())+ "------------------------------------------------")
    #     print("#friends:", len(object.get_friends()))
    #     for ob in object.reference_friends:
    #         print(ob.first_name + " " + ob.last_name + " "+str(ob.health))

    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    #This is a sample test case. Write your own testing code here.
    for i in range(0, 20):
        # all_patient_object = []
        test_result = run_simulation(15, 0.8, 49)
    # test_result = run_simulation(40, 1, 1)
        print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.


    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    # test_result = run_simulation(40, 1, 1)
    #sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

    

# do not add code here (outside the main block).
