

def path_finder(maze):
    maze = maze.splitlines()
    
    stack = [(0, 0)]
    seen = set()
    
    while stack:
        next = stack.pop()
        if next in seen:
            continue
            
        seen.add(next)
        
        x, y = next
      
        if maze[x][y] == "W":
            continue
        
        if x == len(maze) - 1 and y == len(maze) - 1:
            return True
            
        neighbours = _get_neighbours(x, y, maze)
        for n in neighbours:
            if n in seen:
                continue        
            stack.append(n)
    return False
    
def _get_neighbours(x, y, maze):
    positions = (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1)
    )
    neighbours = []
    for pos in positions:
        x, y = pos
        if 0 <= x < len(maze) and 0 <= y < len(maze):
            neighbours.append((x, y))
    return neighbours
