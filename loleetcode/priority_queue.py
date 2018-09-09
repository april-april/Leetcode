# heap queue playground
import heapq

def main():
    random_list = [5, 7, 9, 1, 3, 0, 12]
    # using heapify to convert list into heap 
    heapq.heapify(random_list)  
    # printing created heap 
    print("The created heap is : ", end="") 
    print(list(random_list)) 
    heapq.heappush(random_list, -1) 
    print(list(random_list)) 
    print(heapq.heappushpop(random_list, 2)) 
    heapq.heappush(random_list, -5)

    # using nlargest to print 3 largest numbers 
    print("The 3 largest numbers in list are : ",end="") 
    print(heapq.nlargest(3, random_list)) 

    # using nsmallest to print 3 smallest numbers 
    print("The 3 smallest numbers in list are : ",end="") 
    print(heapq.nsmallest(3, random_list)) 



if __name__ == "__main__":
    main()