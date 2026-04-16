# RoomLight — Test Cases

## TEST-001 Create profile

Command:
create_profile Relax 40 warm

Expected:
Profile is created successfully

---

## TEST-002 Add room

Command:
add_room 101

Expected:
Room is added successfully

---

## TEST-003 Apply profile to all rooms

Command:
apply_profile Relax

Expected:
All rooms use the Relax profile

---

## TEST-004 Apply profile to single room

Command:
apply_profile_to_room 102 Work

Expected:
Room 102 uses Work profile, others remain unchanged

---

## TEST-005 Reset room

Command:
reset_room 102

Expected:
Room 102 has no profile assigned
