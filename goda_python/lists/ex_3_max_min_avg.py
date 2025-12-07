"""
 Rewrite the program that prompts the user for a list of numbers and prints out the
 maximum and minimum of the numbers at the end when the user enters “done”.
 Write the program to store the numbers the user enters in a list and use the max()
 and min() functions to compute the maximum and minimum numbers after the
 loop completes.
"""
list_nums = list()
try:
    while True:
        num_entered = input("Enter a number: ")
        if num_entered == "done":
            maximum = max(list_nums)
            minimum = min(list_nums)
            average = sum(list_nums)/len(list_nums)
            print(f"Maximum: {maximum}\nMininmum: {minimum}\nAverage: {average}")
            break
        flot_num = float(num_entered)
        list_nums.append(flot_num)
except Exception as e:
    print(f"Error: {e}")