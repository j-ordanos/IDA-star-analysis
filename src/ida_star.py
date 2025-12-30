"""
Iterative Deepening A* (IDA*) for Grid Pathfinding
--------------------------------------------------
"""

import math


def manhattan(a, b):
    """
    Manhattan distance: |x1-x2| + |y1-y2|
    Admissible heuristic for grid movement (up/down/left/right)
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def ida_star(start, goal, grid, heuristic=manhattan):

    # Initial bound = heuristic estimate to goal
    threshold = heuristic(start, goal)

    def dfs_search(node, g_cost, current_threshold, visited):
        
        # f(n) = g(n) + h(n)
        f_cost = g_cost + heuristic(node, goal)

        # Prune branches exceeding current threshold
        if f_cost > current_threshold:
            return f_cost

        # Goal check
        if node == goal:
            return "FOUND"

        min_exceed = math.inf

        # Explore neighbors (right, down, left, up)
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (node[0] + dr, node[1] + dc)

            # Boundary and obstacle check
            if not (0 <= neighbor[0] < len(grid) and 
                    0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
            if neighbor in visited:
                continue

            visited.add(neighbor)
            result = dfs_search(neighbor, g_cost + 1, current_threshold, visited)

            if result == "FOUND":
                return "FOUND"

            # Track minimum exceeded f-cost for next iteration
            min_exceed = min(min_exceed, result)
            visited.remove(neighbor)

        return min_exceed

    # Main IDA* loop
    while True:
        visited = {start}  # Track visited nodes in current iteration
        result = dfs_search(start, 0, threshold, visited)

        if result == "FOUND":
            return True
        if result == math.inf:  # No path exists
            return False

        # Increase threshold for next iteration
        threshold = result


# ============================================================================
# EXAMPLE USAGE & TESTING
# ============================================================================
if __name__ == "__main__":
    # Example grid: 0 = free cell, 1 = obstacle
    test_grid = [
        [0, 0, 0, 0, 0],   # Row 0
        [1, 1, 0, 1, 0],   # Row 1 (obstacles at (1,0), (1,1), (1,3))
        [0, 0, 0, 1, 0],   # Row 2 (obstacle at (2,3))
        [0, 1, 1, 1, 0],   # Row 3 (obstacles at (3,1), (3,2), (3,3))
        [0, 0, 0, 0, 0]    # Row 4
    ]

    # Test cases
    test_cases = [
        # (start, goal, expected_result, description)
        ((0, 0), (4, 4), True, "Clear diagonal path"),
        ((0, 0), (1, 2), True, "Path around obstacles"),
        ((0, 0), (3, 1), False, "Blocked by obstacles"),
        ((4, 4), (0, 0), True, "Reverse path"),
    ]

    print("=" * 60)
    print("IDA* ALGORITHM DEMONSTRATION")
    print("=" * 60)

    for i, (start, goal, expected, desc) in enumerate(test_cases, 1):
        print(f"\nTest {i}: {desc}")
        print(f"  Start: {start}, Goal: {goal}")
        
        result = ida_star(start, goal, test_grid)
        
        print(f"  Result: {'PATH FOUND' if result else 'NO PATH'}")
        print(f"  Expected: {'PATH FOUND' if expected else 'NO PATH'}")
        print(f"  Status: {'✓ PASS' if result == expected else '✗ FAIL'}")

    # Quick usage example
    print("\n" + "=" * 60)
    print("MINIMAL USAGE EXAMPLE:")
    print("=" * 60)
    
    # Create your own grid
    custom_grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    
    # Find path from top-left to bottom-right
    path_exists = ida_star((0, 0), (2, 2), custom_grid)
    print(f"\nGrid size: 3x3")
    print(f"Path from (0,0) to (2,2): {'Exists' if path_exists else 'Blocked'}")

    print("\n" + "=" * 60)
    print("Note: This implementation returns boolean only.")
    print("For path reconstruction, modify to track parent pointers.")
    print("=" * 60)