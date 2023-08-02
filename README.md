# Maze-Solver
The Maze Solver is a Python program that uses Pygame to generate and solve mazes using two different algorithms: A* and Depth-First Search (DFS). The program generates a random maze, then finds a path from a random start point to a random goal point using both algorithms. The paths found by the algorithms are then animated on the screen.

## Features
* Maze Generation: The program generates a random maze using a depth-first search algorithm.
* Pathfinding: The program uses both the A* and DFS algorithms to find a path from a random start point to a random goal point in the maze.
* Animation: The program uses Pygame to animate the maze generation and pathfinding process.

## Preview
![Maze Solver Demo](https://github.com/Milosz-cat/Maze-Solver/blob/main/Preview/maze_animation.gif)

### Prerequisites

Make sure you have Python >=3.10 installed on your machine. You can download it from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/Milosz-cat/Maze-Solver.git 
    cd Maze-Solver
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m .venv venv
    
    .\.venv\Scripts\activate (windows)
    or
    source .venv/bin/activate (linux)
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Now you can start the script by typing following command:
```bash
python maze.py
or
python3 maze.py
or
py maze.py
```

This will generate a new maze, solve it, and save a visualization of the maze.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
