name = input("name: ")
family = {
    "Darth Vader":	"father",
    "Leia":	"sister",
    "Han": "brother in law",
    "R2D2":	"droid"
    }
def relation_to_luke(name, family):
    for key, value in family.items():
        if key == name:
            return "Luke, I am your " + value + "."

print(relation_to_luke(name, family))