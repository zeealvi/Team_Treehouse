

attendees = ["Ken", "Lisa", "Zeeshan"]
attendees.append("Ashley")
attendees.extend(["James","Gill"])
optional_invitees = (["Ben", "Ali", "Clark"])
potential_attendees = attendees + optional_invitees
print ("There are", len(potential_attendees), "attendees currently")

for attendee in potential_attendees:
    print (attendee)