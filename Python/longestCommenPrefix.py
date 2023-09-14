def longestCommonPrefix(self, strs: List[str]) -> str:
    ans=""

    strs = sorted(strs) 

    first = strs[0]
    last = strs[-1] 

    for i in range(min(len(first),len(last))): 
        if(first[i]!=last[i]): 
            break
        ans+=first[i]
        
    return ans 

'''
    case : 1 expected output : ""
        input :  ['xyz' , 'acb' , 'abcd'] 

        sorted : ['abcd' ,'acb','xyz'] 

        first : 'abcd' 
        last : 'xyz' 
        when 1 i = 0 -> 'a' != 'x' = true, output -> ''
        output : ''


    case : 2 expected output : "f"
        input : ['flower' , 'fly' , 'four'] 

        sorted =  ['flower','fly','four']

        first : 'flower'
        last : 'four'
        when i = 0 -> 'f' != 'f' == false, output -> 'f'
        when i = 1 -> l' != 'o' = true, output -> 'f'
        output : 'f'

    ### Algorithem ###

    step 1 : sort array by alphabetical order -> ['abcd' ,'acb','xyz'] ,
    step 2 : take first and last element of list
        output = ''
       
    step 3 : iterate of min length of first and last 
        for i in (min(len(first),len(last))) -> 3 ('xyz') 

            if first letter of 'first' and first letter of 'last' are not eqaual  -> 
                then break 
            else 
                add first comman letter to output 
    step 4 :
        return output

'''