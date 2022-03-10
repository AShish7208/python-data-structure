def dac_max(a,index,l):

    max = -1

    if (index>=l-2):
        if a[index]>a[index+1]:
            return a[index]
        else:
            return a[index+1]


    max = dac_max(a,index+1,l)

    if (a[index]>max):
        return a[index]
    else:
        return max


def dac_min(a,index,l):
    min=0

    if(index>=l-2):
        if a[index]<a[index+1]:
            return a[index]
        else:
            return a[index+1]


    min = dac_min(a,index+1,l);


    if (a[index]<min):
        return a[index]
    else:
        return min


if __name__ == '__main__':
   
    # Defining the variables
    min, max = 0, -1;
 
    # Initializing the array
    a = [70, 250, 50, 80, 140, 12, 14];
 
    # Recursion - DAC_Max function called
    max = dac_max(a, 0, 7);
 
    # Recursion - DAC_Max function called
    min = dac_min(a, 0, 7);
    print("The minimum number in a given array is : ", min);
    print("The maximum number in a given array is : ", max);





    

    
