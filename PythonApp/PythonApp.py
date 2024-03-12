#Sample Lorem ipsum text
text = """Lorem ipsum doLor sit3 amet, consectetur adipiscing, elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Consectetur lorem donec massa: sapien ?faucibus et molestie. Sit amet commodo nulla facilisi nullam.
    Volutpat ac tincidunt vitae semper quis lectus nulla at volutpat. Odio eu feugiat pretium nibh ipsum."""

#Casting to list so can modify that
list_text = list(text)

#for loop through the list
for i in range(len(list_text)):
    #check if 'i' refer to first or last character of string
    if i == 0 or i == len(list_text) - 1:
        if list_text[i].isalpha():
            list_text[i] = list_text[i].upper()
        continue
    #upper the first or last letter of each word
    if list_text[i].isalpha():
        if not list_text[i - 1].isalpha() or not list_text[i + 1].isalpha():
            list_text[i] = list_text[i].upper()

#items of list will join together to make final text
final_text = ''.join(list_text)

print(final_text)