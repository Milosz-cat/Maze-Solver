import pygame
import random
import time

# Maze dimensions
WIDTH = 40
HEIGHT = 40
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Size of a single cell in the maze
CELL_SIZE = 20

# Set the window size
WINDOW_SIZE = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pathfinding Animation")

# Generate the maze
maze = [[0] * WIDTH for _ in range(HEIGHT)]


def generate_maze():
    stack = [(0, 0)]

    while stack:
        current = stack[-1]
        x, y = current

        neighbors = []

        if x > 1 and maze[x - 2][y] == 0:
            neighbors.append((x - 2, y))
        if x < WIDTH - 2 and maze[x + 2][y] == 0:
            neighbors.append((x + 2, y))
        if y > 1 and maze[x][y - 2] == 0:
            neighbors.append((x, y - 2))
        if y < HEIGHT - 2 and maze[x][y + 2] == 0:
            neighbors.append((x, y + 2))

        if neighbors:
            next_cell = random.choice(neighbors)
            nx, ny = next_cell
            maze[nx][ny] = 1
            maze[(x + nx) // 2][(y + ny) // 2] = 1
            stack.append(next_cell)
        else:
            stack.pop()


# Function to draw the maze on the screen
def draw_maze():
    screen.fill(BLACK)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if maze[x][y] == 0:
                pygame.draw.rect(
                    screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    pygame.display.flip()


# Initialize maze generation
generate_maze()
draw_maze()


# Choose random start and goal points
def choose_random_point():
    while True:
        x = random.randint(1, WIDTH - 2)
        y = random.randint(1, HEIGHT - 2)
        if maze[x][y] == 1:
            return (x, y)


start_node = choose_random_point()
goal_node = choose_random_point()

while start_node == goal_node:
    goal_node = choose_random_point()


# A* algorithm heuristic function
def heuristic(node, goal):
    u, v = node
    p, q = goal
    return abs(u - p) + abs(v - q)


# Get neighboring cells of a node
def get_neighbors(node):
    x, y = node
    neighbors = []

    if x > 0 and maze[x - 1][y] == 1:
        neighbors.append((x - 1, y))
    if x < WIDTH - 1 and maze[x + 1][y] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and maze[x][y - 1] == 1:
        neighbors.append((x, y - 1))
    if y < HEIGHT - 1 and maze[x][y + 1] == 1:
        neighbors.append((x, y + 1))

    return neighbors


# A* algorithm for pathfinding
def astar_search(start, goal):
    frontier = [(start, 0)]
    visited = set()
    path = {}
    g = {start: 0}
    f = {start: heuristic(start, goal)}

    while frontier:
        frontier.sort(key=lambda x: f[x[0]])
        current, _ = frontier.pop(0)
        visited.add(current)

        if current == goal:
            # Found the goal - reconstruct the path
            path_cost = g[current]
            optimal_path = [current]

            while current != start:
                current = path[current]
                optimal_path.append(current)

            optimal_path.reverse()
            return optimal_path, path_cost

        neighbors = get_neighbors(current)

        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = g[current] + 1

                if neighbor not in g or new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    f[neighbor] = g[neighbor] + heuristic(neighbor, goal)
                    path[neighbor] = current

                    if neighbor not in frontier:
                        frontier.append((neighbor, f[neighbor]))

        # Draw the current search state
        draw_maze_with_path(path, current, start, goal)
        pygame.time.wait(10)

    return None


# Depth-First Search (DFS) algorithm for pathfinding
def dfs_search(start, goal):
    stack = [start]
    visited = set()
    path = {}

    while stack:
        current = stack.pop()
        visited.add(current)

        if current == goal:
            # Found the goal - reconstruct the path
            path_cost = len(path)
            optimal_path = [current]

            while current != start:
                current = path[current]
                optimal_path.append(current)

            optimal_path.reverse()
            return optimal_path, path_cost

        neighbors = get_neighbors(current)

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                path[neighbor] = current

        # Draw the current search state
        draw_maze_with_path(path, current, start, goal)
        pygame.time.wait(10)

    return None


# Function to draw the maze with the current search state
def draw_maze_with_path(path, current, start, goal):
    screen.fill(BLACK)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if maze[x][y] == 0:
                pygame.draw.rect(
                    screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

    for node in path:
        if node != start and node != goal:
            x, y = node
            pygame.draw.rect(
                screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    pygame.draw.rect(
        screen, BLUE, (start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )
    pygame.draw.rect(
        screen, BLUE, (goal[0] * CELL_SIZE, goal[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )
    pygame.draw.rect(
        screen,
        RED,
        (current[0] * CELL_SIZE, current[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )

    pygame.display.flip()


# Initialize variables to store path information
astar_path = []
astar_path_cost = 0
dfs_path = []
dfs_path_cost = 0

start_time = time.time()
# Find the path using A* algorithm
astar_result = astar_search(start_node, goal_node)
end_time = time.time()

if astar_result:
    astar_path, astar_path_cost = astar_result
    print("Found path [A*]:", astar_path)
    print("Cost [A*]:", astar_path_cost)
    print("Execution time [A*]:", end_time - start_time, "seconds")
else:
    print("Path not found [A*].")

# Generate a new maze
generate_maze()
draw_maze()

start_time = time.time()
# Find the path using DFS algorithm
dfs_result = dfs_search(start_node, goal_node)
end_time = time.time()

if dfs_result:
    dfs_path, dfs_path_cost = dfs_result
    print("Found path [DFS]:", dfs_path)
    print("Cost [DFS]:", dfs_path_cost)
    print("Execution time [DFS]:", end_time - start_time, "seconds")
else:
    print("Path not found [DFS].")

# Main program loop
running = True
animation_speed = 10
astar_finished = False
dfs_finished = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        break

    # Draw the current search state for A* algorithm
    if astar_path and not astar_finished:
        draw_maze_with_path(astar_path, goal_node, start_node, goal_node)
        pygame.time.wait(animation_speed)
        astar_finished = True
        pygame.time.wait(3000)
        generate_maze()
        draw_maze()

    # Draw the current search state for DFS algorithm
    elif dfs_path and not dfs_finished:
        draw_maze_with_path(dfs_path, goal_node, start_node, goal_node)
        pygame.time.wait(animation_speed)
        dfs_finished = True
        pygame.time.wait(3000)
        generate_maze()
        draw_maze()

    if astar_finished and dfs_finished:
        running = False

pygame.quit()
