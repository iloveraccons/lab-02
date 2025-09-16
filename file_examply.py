with open('sample.txt','r') as f:
    for idx, line in enumerate(f, start=1):
        print(f"{idx}: {line.strip()}")