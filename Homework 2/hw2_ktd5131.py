class MySorted(): 
    
    def bubble_sorted(iterable,key=None,reverse=False):
        global comparisons
        comparisons = 0
        global swaps
        swaps = 0
        key = key
        iterable = iterable
        reverse = reverse
        
        # 1) Transform to list
        if type(iterable) != list:
            srtd_lst=[el for el in iterable] #Transform to list via list comprehension
        
        # 2) bubble sort list
        srtd_lst=[]+iterable # Leaves original list unaltered; Courtesy of Joe Baka
        
        # 2.1) Handling Two Edge cases
        if len(srtd_lst) == 1 and type(srtd_lst[0] != str): 
            return srtd_lst
        
        if len(srtd_lst) == 1 and type(srtd_lst[0] == str): # Handling Edge case
            srtd_lst=[el for el in srtd_lst[0]]
            return srtd_lst
        
        # 2.2) Main Bubble Sort Code
        # 2.2.1) With provided key
        srtd_lst=[]+iterable # Leaves original list unaltered; Courtesy of Joe Baka
        switch = 1
        if key != None:
            while switch != 0: # Keep doing runs through the list while making at least one switch
                switch = 0
                for i in range(len(srtd_lst)-1): # This is one run
                    comparisons += 1
                    if key(srtd_lst[i]) > key(srtd_lst[i+1]):
                        srtd_lst[i], srtd_lst[i+1] = srtd_lst[i+1], srtd_lst[i]
                        swaps+=1
                        switch+=1
        # 2.2.2) Without provided key
        else:
            while switch != 0: # Keep doing runs while making at least one switch
                switch = 0
                for i in range(len(srtd_lst)-1): # This is one run
                    comparisons += 1
                    if srtd_lst[i] > srtd_lst[i+1]:
                        srtd_lst[i], srtd_lst[i+1] = srtd_lst[i+1], srtd_lst[i]
                        swaps+=1
                        switch+=1
            
        # 3) if reverse = True --> reverse list
        if reverse==True:
            srtd_lst=srtd_lst[::-1]
        print("This program performed ",comparisons," comparisons and ",swaps," swaps.")
        return srtd_lst, comparisons, swaps
    
    # ------------------- MERGE SORTING CODE -------------------
    def splt(lst):
        length = len(lst)
        mid = int(length/2)
        return lst[:mid], lst[mid:]

    def merge( lst1, lst2, key = None):
        global comparisons
        comparisons = comparisons
        mrgd_lst=[]
        i=0
        j=0
        key = key
        if key == None:
            while i < len(lst1) and j < len(lst2):
                comparisons += 1
                if lst1[i] < lst2[j]:
                    mrgd_lst.append(lst1[i])
                    i += 1
                else:
                    mrgd_lst.append(lst2[j])
                    j += 1
        else:
            while i < len(lst1) and j < len(lst2):
                comparisons += 1
                if key(lst1[i]) < key(lst2[j]):
                    mrgd_lst.append(lst1[i])
                    i += 1
                else:
                    mrgd_lst.append(lst2[j])
                    j += 1
        if i == len(lst1):
            mrgd_lst = mrgd_lst + lst2[j:]
        else:
            mrgd_lst = mrgd_lst + lst1[i:]
        return mrgd_lst
    
    def merge_sort(lst, key = None): 
        key = key
        if len(lst) <= 1:
            return lst
        else:
            lst1, lst2 = MySorted.splt(lst)
        return MySorted.merge(MySorted.merge_sort(lst1, key), MySorted.merge_sort(lst2, key), key)
        # 3) if reverse = True --> reverse list
    def merge_sorted(lst, key = None, reverse = False):
        global comparisons
        comparisons = 0
        key = key
        if reverse == True:
            return MySorted.merge_sort(lst, key)[::-1], comparisons
        else:
            return MySorted.merge_sort(lst, key), comparisons
    