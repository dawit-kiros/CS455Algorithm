def hasPath(maze, start, destination):
    # Define directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        if [x, y] == destination:
            return True
        
        # Mark the current cell as visited
        maze[x][y] = 2
        
        for dx, dy in directions:
            # Keep moving in a certain direction until you hit a wall or reach the boundary
            newX, newY = x + dx, y + dy
            while 0 <= newX < len(maze) and 0 <= newY < len(maze[0]) and maze[newX][newY] != 1:
                newX += dx
                newY += dy
            
            # Backtrack and explore other directions
            if dfs(newX - dx, newY - dy):
                return True
        
        return False
    
    return dfs(start[0], start[1])

# Test data
maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

print(hasPath(maze, start, destination))  # Output: True
