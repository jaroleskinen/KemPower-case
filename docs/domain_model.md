# RoomLight — Domain Model

## Overview

This domain model describes the main concepts of the RoomLight system and how they relate to each other.

The goal is to define a shared understanding of the system before moving to implementation.

---

## Main Concepts

### Hotel
Represents a hotel that contains multiple rooms.

### Room
Represents a single hotel room. Each room has its own lighting settings and status.

### LightingProfile
A predefined set of lighting settings (e.g. brightness, mode) that can be applied to rooms.

### RoomType
Defines different types of rooms (e.g. standard, suite), which may use different lighting configurations.

### Guest
Represents a hotel guest who can adjust lighting in their room.

### Staff
Represents hotel staff who manage lighting settings and profiles.

### LightingState
Represents the current lighting settings active in a room.

---

## Relationships

- A Hotel contains multiple Rooms  
- A Room belongs to one Hotel  
- A Room uses one LightingProfile  
- A LightingProfile can be used by multiple Rooms  
- A Room has one current LightingState  
- Staff can create and update LightingProfiles  
- Staff can apply a LightingProfile to one or more Rooms  
- A Guest can modify the LightingState of their room  
- A Room is associated with one RoomType  

---

## Simple Diagram

    Hotel
      |
      +-- Room
      |     |
      |     +-- LightingState
      |     |
      |     +-- LightingProfile
      |     |
      |     +-- RoomType
      |
      +-- Staff --- manages ---> LightingProfile
      |
      +-- Guest --- modifies --> LightingState

---

## Notes

This model focuses on the core concepts needed for the prototype:

- Define lighting settings  
- Apply them to rooms  
- View and modify room lighting  

The model avoids technical details and focuses only on the structure of the system.
