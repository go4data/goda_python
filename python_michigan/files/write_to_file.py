try:
    with open("open_file.txt","r") as source_file:
        lines = source_file.readlines()
    
    with open("shouting.txt","w") as file:
        for line in lines:
            file.write(line.upper())
    print("File 'shouting.txt' has been created successfully!")
    print(f"Converted {len(lines)} lines from 'open_file.txt' to upper case into 'shouting.txt'")

except FileNotFoundError:
    print("Error: open_file.txt not found")
except Exception as e:
    print(f"An error occurred: {e}")