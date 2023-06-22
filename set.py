# Email list from Source A
list_a = {'email1@example.com', 'email2@example.com', 'email3@example.com'}

# Email list from Source B
list_b = {'email3@example.com', 'email4@example.com', 'email5@example.com'}

# Merge the email lists using union
merged_list = list_a | list_b

# Display the merged email list
print("Merged Email List:")
for email in merged_list:
    print(email)
    

