import re
ips = []  # creates an empty list called ips
with open('auth.log', 'r') as f:
    for line in f:
        found_ips = re.findall(r"\d+\.\d+\.\d+\.\d+", line)
        for ip in found_ips:
            ips.append(ip)  # Add each ip to our list
            print(ip)
# Convert to a set to remove duplicates
unique_ips = set(ips)

# Print each unique IP
print("Unique IPs:")
for ip in unique_ips:
    print(ip)

# Write unique IPs to unique_ips.txt, one per line
with open('unique_ips.txt', 'w') as dst:
    for ip in sorted(unique_ips):
        dst.write(ip + '\n')
print(ips)
