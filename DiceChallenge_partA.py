def total_number_of_combinations(die_a,die_b):
    ct=0
    for i in die_a:
        for j in die_b:
            ct+=1
    return ct

def distribution_matrix(die_a,die_b):
    distribution = [[(i, j) for j in range(1, len(die_a))] for i in range(1, len(die_b))]
    for row in distribution:
        # row = [(1,1),(1,2),(1,3),(1,4),(1,5),(1,6)] for i=1
        print(row)


def calculate_probabilities(die_a, die_b):
    total_outcomes=len(die_a)*len(die_b)  
    probabilities={}
    for outcome in range(2, 13):
        count= 0
        for faceA in die_a:
            for faceB in die_b:
                if faceA+faceB==outcome:
                    count+= 1
        
        probability=count/total_outcomes
        probabilities[outcome]=probability

    for key, val in probabilities.items():
        print('P(Sum = '+str(key)+') = '+str(round(val, 4))) 

        
die_a=[1,2,3,4,5,6]
die_b=[1,2,3,4,5,6]

total_combinations_number=total_number_of_combinations(die_a, die_b)
print('The total possible combinations are: '+str(total_combinations_number))

print('\nDistribution Matrix:')
distribution_matrix(die_a, die_b)

print('\nProbabilities:')
calculate_probabilities(die_a, die_b)