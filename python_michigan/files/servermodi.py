try:
    # First, let's check if the file exists and see its content
    with open("server.log", "r") as source:
        print("File opened successfully! Here are the first few lines:")
        lines = source.readlines()
        
        if not lines:
            print("File is empty!")
        else:
            print(f"Total lines: {len(lines)}")
            print("First 5 lines:")
            for i, line in enumerate(lines[:5], 1):
                print(f"{i}: {line.strip()}")
    
    # Now let's search with debugging
    print("\nSearching for log messages...")
    counts = {'ERROR': 0, 'INFO': 0, 'WARNING': 0}
    
    with open("server.log", "r") as source:
        for line_num, line in enumerate(source, 1):
            line_upper = line.upper()
            
            # Debug: print what we're checking
            if any(msg in line_upper for msg in ['ERROR', 'INFO', 'WARNING']):
                print(f"Line {line_num}: {line.strip()}")
            
            for msg_type in counts:
                if f"{msg_type}:" in line_upper:
                    counts[msg_type] += 1
                    print(f"✓ Found {msg_type} at line {line_num}")
                    break
    
    print(f"\nFinal counts: {counts}")
    
    # Generate report
    if sum(counts.values()) == 0:
        print("No log messages found! Check your file format.")
    else:
        most_frequent = max(counts, key=counts.get)
        max_count = counts[most_frequent]
        
        with open("report.txt", "w") as summary:
            summary.write("Log File Analysis Report\n")
            summary.write("=" * 25 + "\n")
            for msg_type, count in counts.items():
                summary.write(f"{msg_type}: {count}\n")
            summary.write("=" * 25 + "\n")
            summary.write(f"Most Frequent: {most_frequent} ({max_count} occurrences)\n")
        
        print("✓ Report generated: report.txt")
        
except FileNotFoundError:
    print("✗ Error: server.log file not found in current directory")
    print("Make sure server.log is in the same folder as your Python script")
except Exception as e:
    print(f"✗ Error: {e}")