attendees = ["Ken", "Lisa", "Zeeshan"]
attendees.append("Ashley")
attendees.extend(["James","Gill"])
optional_invitees = (["Ben", "Ali", "Clark"])
potential_attendees = attendees + optional_invitees
print ("There are", len(potential_attendees), "attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)

print ("To:" + to_line)
print ("CC:" + cc_line)
to_line.split(", ")