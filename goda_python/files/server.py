count_err = 0
count_inf = 0
count_warn = 0
try:
    with open("server.log", "r") as source, open("report.txt","w") as summary:
        for line in source:
            line_upper = line.upper()
            if "ERROR:" in line_upper:
                count_err += 1
            elif("INFO:" in line_upper):
                count_inf += 1
            elif("WARNING:" in line_upper):
                count_warn += 1
            else:
                continue
        summary.write(f"The count of \n\t Error messages = {count_err}\n\t Warning messages = {count_warn}\n\t Info messages = {count_inf}\nThe most frequent type of log messages is{max(count_inf,count_err, count_warn)}")
except FileNotFoundError:
    print("Error: this folder not found")
except Exception as e:
    print(f"Error message as {e}")
