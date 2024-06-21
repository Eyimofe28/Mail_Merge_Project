# Getting all the names from the invited names text file.
with open("../Mail_Merge_Project/Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

    # Creating new letter for each name by replacing the [name] placeholder with actual names.
    with open("../Mail_Merge_Project/Input/Letters/starting_letter.txt", "r") as file2:
        letter_content = file2.readlines()
        for i in names:
            i = i.strip()
            letter_content[0] = letter_content[0].replace("[name]", i)

            # Saving them in the folder "ReadyToSend".
            with open(f"../Mail_Merge_Project/Output/ReadyToSend/letter_to_{i}", "w") as file3:
                for sentence in letter_content:
                    file3.write(sentence)
