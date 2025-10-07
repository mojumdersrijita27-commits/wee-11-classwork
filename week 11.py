def main():
    try:
        # Try to open the file
        infile = open("Salaries.txt", "r")  # FileNotFoundError if fails

        # Try to read and convert the salary
        salary = int(infile.readline().strip())  # ValueError if fails
        print("Salary:", salary)

    except FileNotFoundError:
        print("File Salaries.txt not found.")

    except ValueError:
        print("File Salaries.txt contains an invalid salary.")

    else:
        # Close file if no exception occurred
        infile.close()

    finally:
        # Always executes
        print("Thank you for using our program.")


# Run the main function
if __name__ == "__main__":
    main()
