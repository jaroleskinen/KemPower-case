# RoomLight — Test Plan

## Scope

This test plan covers the core functionality of the RoomLight CLI prototype:

- creating lighting profiles  
- adding rooms  
- applying profiles to all rooms  
- applying profile to a single room  
- resetting a room  

Non-functional requirements such as performance or security are not tested in this prototype.

---

## Approach

Testing is done manually by running commands in the terminal.

Each command is tested separately and the results are verified based on expected output.

---

## Environment

- VS Code terminal  
- Python 3  

---

## Pass Criteria

A test is considered successful if:

- the command runs without errors  
- the output matches the expected result  
- the system state is updated correctly  

---

## Risks

- invalid input may cause unexpected behavior  
- missing data file may affect results  
