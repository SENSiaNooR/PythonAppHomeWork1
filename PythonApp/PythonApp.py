text = """Lorem ipsum doLor sit3 amet, consectetur adipiscing, elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Consectetur lorem donec massa: sapien ?faucibus et molestie. Sit amet commodo nulla facilisi nullam.
    Volutpat ac tincidunt vitae semper quis lectus nulla at volutpat. Odio eu feugiat pretium nibh ipsum."""

list_text = list(text)
for i in range(len(list_text)):
    if i == 0 or i == len(list_text) - 1:
        if list_text[i].isalpha():
            list_text[i] = list_text[i].upper()
        continue
    if list_text[i].isalpha():
        if not list_text[i - 1].isalpha() or not list_text[i + 1].isalpha():
            list_text[i] = list_text[i].upper()

final_text = ''.join(list_text)

print(final_text)