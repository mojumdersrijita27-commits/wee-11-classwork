def main():
    try:
        
        infile = open("Salaries.txt", "r")  

        
        salary = int(infile.readline().strip())  
        print("Salary:", salary)

    except FileNotFoundError:
        print("File Salaries.txt not found.")

    except ValueError:
        print("File Salaries.txt contains an invalid salary.")

    else:
        
        infile.close()

    finally:
        
        print("Thank you for using our program.")



if __name__ == "__main__":
    main()

