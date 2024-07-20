# Fermat's Last Theorem Near Misses
# File Name: assignment1_fermat.py
# External files: None
# Programmers: Abhivardhan Tammana , Sireesha Reddy Bijjam
# Course: Software Engineering, CPSC 60500, Section 1
# Date: 7/20/2024
# Description: This program searches for "near misses" of the form (x, y, z, n, k) in the formula x^n + y^n = z^n,
# where x, y, z, n, k are positive integers, and outputs the smallest relative miss found.

import math

def find_near_misses(n, k):
    smallest_miss = float('inf')
    #storing the values of x,y,z,miss for smallest possible miss found
    best_x = best_y = best_z = 0 
    actual_miss = 0 
    count=0 # counting the possible number of miss values
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            xn_yn = x**n + y**n
            #Finding the value of z
            z = int(math.pow(xn_yn, 1/n))
            zn = z**n
            zn_plus_1 = (z + 1)**n
            
            #caliculating the misses for z^n and (z+1)^n with x^n + y^n
            miss1 = abs(xn_yn - zn)
            miss2 = abs(xn_yn - zn_plus_1)
            miss = min(miss1, miss2)
            relative_miss = miss / xn_yn
            
            #Finding the new smallest miss
            if relative_miss < smallest_miss:
                count=count+1
                smallest_miss = relative_miss
                best_x, best_y, best_z = x, y, z if miss1 < miss2 else z + 1
                actual_miss = miss
                print("\n=====MINIMUM MISS OBSERVED=====")
                print(f"x = {x}, y = {y}, z = {best_z}\nactual miss = {actual_miss}\nrelative miss = {smallest_miss:.10f}")

    print(f"\n##### SMALLEST RELATIVE MISS AMONG {count} OTHER MISSESS #####")
    print(f"x = {best_x}, y = {best_y}, z = {best_z}\nactual miss = {actual_miss}\nrelative miss = {smallest_miss:.10f}")

def main():
    #User input n,k
    while True:
        try:
            n = int(input("Enter the power n (3 <= n < 12): "))
            if 3 <= n < 12:
                break
            else:
                print("Invalid input. Please ensure 3 <= n < 12.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            k = int(input("Enter the limit k (k > 10): "))
            if k > 10:
                break
            else:
                print("Invalid input. Please ensure k > 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    find_near_misses(n, k)

if __name__ == "__main__":
    while True:
        main()
        # searching for other near misses based on user input
        user=input("\n\ndo you want to explore Smallest misses for other values of n,k ?\ntype yes/no \nyour answer : ")
        if user=="yes" or user=="YES" or user=="Yes":
            continue
        else:
            break
