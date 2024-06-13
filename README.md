# Elevator Challenge

Elevator Challenge is a simulation program built with Pygame that simulates multiple elevators moving between floors in response to user requests.

## Features

- Simulates multiple elevators and floors.
- Handles user requests via mouse clicks.
- Displays the current state of elevators and floors.
- Plays a sound when an elevator arrives at a floor.


 **Add necessary resources:**

    Place the following files in the project root directory:
    - `elv.png`
    - `building.png`
    - `ding.mp3`

## Project Structure

- **`main.py`**: Initializes the Pygame environment, loads images, initializes the `Building` instance, and runs the main event loop.
- **`my_setting.py`**: Contains configuration constants for display settings, colors, and simulation parameters.
- **`building_floor_elv.py`**: Contains class definitions for `Building`, `Floor`, `Button`, and `Elv`.

## Class Responsibilities

### `Building`
- Manages multiple `Elv` (elevators) and `Floor` instances.
- Handles user requests by detecting mouse clicks and directing the appropriate elevator to the requested floor.
- Updates and draws all elevators and floors on the screen.

### `Floor`
- Represents a single floor in the building.
- Manages a button for requesting an elevator.
- Tracks the timer for how long an elevator will take to reach the floor.
- Updates and draws the floor and its button on the screen.

### `Button`
- Represents a button on a floor.
- Detects if it has been pressed based on mouse coordinates.
- Updates its visual state based on whether it has been pressed or not.
- Draws itself on the screen.

### `Elv`
- Represents a single elevator.
- Manages its position, state, and requests.
- Moves between floors based on requests.
- Updates its position and state over time.
- Draws itself on the screen.

## Usage

- Click on the buttons next to each floor to request an elevator.
- The elevators will move to the requested floor, and the button will change color to indicate that a request is being processed.
- The elevator will pause briefly when it reaches a requested floor and play a sound.

## Configuration

You can customize the settings of the simulation by modifying the constants in `my_setting.py`. This includes the number of floors and elevators, screen dimensions, and various colors and timings. 
Note that there are variables that are related to others.
Only the magic numbers can be changed



