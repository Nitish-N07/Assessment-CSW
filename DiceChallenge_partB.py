def frequency_of_sums(die_A, die_B):
        frequency = []
        sums = []
        
        for i in range(len(die_A)):
            for j in range(len(die_B)):
                sums.append(die_A[i] + die_B[j])
        # sums = [2,3,3,4,4,4...]   
             
        for i in range(2, 13):
            frequency.append(sums.count(i))
        # frequency = [1,2,3,4,5,6,5,4,3,2,1]
        
        return frequency
    
    
def combinations(list, combo_length):
        # list = [1,2,3]
        # combo_length = 2
        if combo_length == 0:
            return [[]]
        
        result_combinations = []
        
        for i in range(len(list)):
            
            selected_element = list[i]
            # selected_element = 1
            remaining_elements = list[i + 1:]
            # remaining_elements = [2,3]
            remaining_combinations = combinations(remaining_elements, combo_length - 1)
            # remaining_combinations = [[2],[3]]
            for remaining_combination in remaining_combinations:
                
                if [selected_element, *remaining_combination] not in result_combinations:
                    result_combinations.append([selected_element, *remaining_combination])
            # result_combinations = [[1,2],[1,3]]
            
        # result_combinations = [[1,2],[1,3],[2,3]]            
        return result_combinations
    
def undo_dice(die_A, die_B):
    
    prob_original = frequency_of_sums(die_A, die_B)
    
    dieA_PossibleElements = [num for num in range(1, 5) for _ in range(6)]
    # dieA_PossibleElements = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3...]
    combinationsOfdieA_elements = combinations(dieA_PossibleElements, len(die_A))
    
    dieB_PossibleElements = [j for j in range(1, 9)]
    # dieB_PossibleElements = [1,2,3,4,5,6,7,8]
    combinationsOfdieB_elements = combinations(dieB_PossibleElements, len(die_B))
    

    for a in combinationsOfdieA_elements:
        for b in combinationsOfdieB_elements:
            prob_pos = frequency_of_sums(a, b)
            if prob_pos == prob_original:
                return a, b

# Example usage
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

New_Die_A, New_Die_B = undo_dice(Die_A, Die_B)

print(f"New_Die_A: {New_Die_A}")
print(f"New_Die_B: {New_Die_B}")