import pandas as pd
import numpy as np
from random import randrange

## supermarket class
class Supermarket:
    def __init__(self, opening, closing, prob_customers, inventory, transition_matrix, start_proba):
        self.opening = opening
        self.closing = closing
        self.prob_customers= prob_customers
        self.inventory = inventory
        print(self.inventory, 'initsuma')
        self.list_customers = []
        self.list_checkout = []
        self.timerange = pd.date_range(start = self.opening, end = self.closing,freq="1Min") ### add frequency of the time intervals
        self.transition_matrix = transition_matrix
        self.start_proba = start_proba
        self.customer_counter = 0

   
    def simulation_movement_market (self):
        for timestamp in self.timerange:
            #here we are moving all customers and move it, if necesary to the list of the checkouts
            for customer in self.list_customers:
                print(self.inventory, 'simmovmar')
                self.inventory = customer.moving_customer(timestamp, self.inventory)
            
            #indexes to be moved
            indexes_of_people_in_checkout = []
            for index, customer in enumerate(self.list_customers):
                if (customer.location == "checkout"):
                    indexes_of_people_in_checkout.append(index)
            for index in indexes_of_people_in_checkout:
                self.list_checkout.append(self.list_customers[index])
            #remove index from back to front to not get the index out of bound problem
            if indexes_of_people_in_checkout:
                for index in indexes_of_people_in_checkout.sort().reverse(): # get reverse sorted index list so to remove the costumers 
                     del self.list_customers[index]

            # based on the probabilty rate we generate customers
            for _ in range(np.random.randint(0,self.prob_customers)):#randrange(0, self.prob_customers):
            # # for loop for person generated
            # # customer generation with an id, timestemp, transitionmatrix, start_proba, inventory
                new_costumer = Customer(id = self.customer_counter, timestamp = timestamp, transimatrix = self.transition_matrix, startprobability = self.start_proba, inventory = self.inventory)
                
                self.inventory = new_costumer.return_inventory()
                
                self.list_customers.append(new_costumer)
                self.customer_counter += 1 #(this is the same as typing = self.customer_counter + 1)
    
    def simulation_movement_checkout (self):
        pass
        #for customer in self.list_checkout: # calculate the chechout time of each customers
        #    customer.checkouttime()
    
    def create_costumer_dataframe(self):
        customer_DF = pd.DataFrame()
        for customer in self.list_checkout: 
            histroy_DF = customer.get_history()
            customer_DF = pd.concat([customer_DF,histroy_DF])
        return customer_DF

class Customer :
    def __init__(self,id,timestamp, transimatrix, startprobability,inventory):
        self.customer_id=id
        self.timestamp=timestamp
        self.transimatrix=transimatrix
        self.startprobability=startprobability
        self.satisfaction_score=0
        self.inventory=inventory
        # calculate location <- start probabilty
        self.location_state(True)
        # calculate missing inventory <- current inventory and the withdrawn inventory
        self.inventory_calculation()
        # calculate satisfaction 
        self.history = pd.DataFrame({"id":self.customer_id,"timestamp":self.timestamp,"location":self.location,
                                        "no_available": self.no_available,"satisfaction_score": self.satisfaction_score},index=[0])
    
    def return_inventory (self):
        return self.inventory
    
    
    def location_state(self,is_start):
        if is_start==False:
            self.location = np.random.choice(self.transimatrix.columns,p=self.transimatrix.loc[self.location])
        else:
            self.location = np.random.choice(self.transimatrix.columns,p=self.startprobability)
    
    def inventory_calculation(self):
        if self.location!='checkout':
            self.num_products_taken = np.random.choice([1,2,3,4])
            print(self.num_products_taken, "HALLO")
            print(self.inventory, 'invcalc') # remove the 0 taken option because some customers dont take anythin while shopping
            self.inventory[self.location]=self.inventory[self.location] - self.num_products_taken
            self.satisfaction_score_calc()
            if self.inventory[self.location] < 0:
                self.inventory[self.location] = 0
            
     
    def satisfaction_score_calc(self):
        if (self.inventory[self.location] > 0):
            self.no_available = 0
            self.satisfaction_score=1
        elif (self.inventory[self.location] < 0):
            self.no_available=self.inventory[self.location] 
            if abs(self.inventory[self.location]) == self.num_products_taken:
                self.satisfaction_score= -1
            else:
                self.satisfaction_score= 0.5      
        
    def moving_customer(self,timestamp,inventory):
        self.inventory=inventory
        self.location_state(False)   
        print(self.inventory, 'movcus')  
        self.inventory_calculation()
        self.current = pd.DataFrame({"id":self.customer_id,"timestamp":timestamp,"location":self.location,
                                    "no_available": self.no_available,"satisfaction_score": self.satisfaction_score},index=[0])
        self.history = pd.concat([self.history,self.current])
        self.return_inventory()
        
    def checkout_list(self):
        pass
    
    
    def get_history(self):
        return self.history

