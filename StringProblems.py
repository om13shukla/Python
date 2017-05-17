class StringProblems:
    def __init__(self,str1):
        self.input_string1 = str1


    def chk_unique_chars(self):
        """Checks if the given String has all unique charecters"""
        temp_string = self.input_string1
        count = 0
        for c in temp_string:
            count=0
            for ch in self.input_string1:
                if (c == ch):
                    count+=1
                if (count > 1):
                    return ch
        return 0

    def str_reverse(self):
        """Reverses the string without using and given Libraries"""
        temp_str = ""
        for i in range(1,(len(self.input_string1)+1)):
            temp_str += self.input_string1[-i]
            #print temp_str
        print temp_str

    def chk_palin(self):
        """Checks if the given string is palinidrome or Not"""
        temp_str = self.input_string1
        lenth = len(self.input_string1)
        ct = 0
        for i in range(0,lenth/2):
            if temp_str[i] +" = "+ temp_str[i-lenth]:
                ct = 0    
            else:
                ct = 1
        if ct:
            print "Not a palin drome",temp_str
        else:
            print "Its Palindrome ",temp_str

    def chk_perm(self):
        """CHecks if the Second given String is a Permutation (Anagram) of
First Given String!""" 
        str1 = raw_input("Enter string 1: ")
        str2 = raw_input("Enter string 2: ")
        
        list1 = list(str1)
        list2 = list(str2)

        list1 = sorted(list1)
        list2 = sorted(list2)

        if len(list1)==len(list2):
            for i,j in zip(list1,list2):
                if i!=j:
                    print str2," is not a Permation of ",str1
                    return 0
            print str2," is A a Permation of ",str1
            
        else:
            print str2," is Not a Permation of ",str1
            
    def replace_space(self):
        """Replaces each 'space' with '%20', Using IN-PLACE replacement:
eg: 'the ring  ' = 'the%20ring' """
        ls1=list(self.input_string1)
        j=i=0
        
        while ' ' in ls1:
            print ls1
            i=ls1.index(' ')
            ls1[i] = '%'
            print "i= ",i
            j=len(ls1)-1
            print "j= ",j
            while j>i+2:
                ls1[j]=ls1[j-2]
                j=j-1
            ls1[i+1]='2'
            ls1[i+2]='0'
            print ls1

    def str_comp(self):
        str1=self.input_string1
        ls1=[]
        count=0
        n=0
        while n<(len(str1)):
            ls1.append(str1[n])
            count=0
            i=n
            while (str1[i]==str1[n]):
                print "str1[",i,"]=",str1[i]," str1[",n,"]=",str1[n]
                count+=1
                i+=1
                if i>(len(str1)-1):
                    break
            n=i
            print "new n=",n
            ls1.append(count)
            print ls1,"\n\n"
#
        if (len(ls1)<len(str1)):
            print "Final Result======\n\n\n"
            print ls1
        else:
            print "Nothing much to Compress"
            print list(str1)
    
        
    def make_zero(self, arr):
        i=j=0
        
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if (arr[i][j]==0):
                    print "found ",arr[i][j]," at arr[",i,"][",j,"]"
        
        for k in range(len(arr[i])):
            arr[i][k]=0    
        for l in range(len(arr)):
            arr[l][j]=0
        for l in range(len(arr)): 
            print arr[l]  
                
            
            
                
            
           
                    
                
        
    
