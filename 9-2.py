last_initial = ["B.", "D.", "H.", "E.", "G.", "G.", "H.", "R.", "M.", "L.", "I.", "I.", "N.", "N.", "O.", "P.", "P.", "X.", "T.", "S.", "S.", "P."]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

for row in rows:
    for index, value in enumerate(row):
        row[index] = "{0} {1}".format(value, last_initial[0])
        del last_initial[0]
print(rows)