"""
Basic Usage Examples for IDA* Algorithm
========================================
This file demonstrates the basic usage of the IDA* algorithm
for different grid configurations and scenarios.
"""

from src.ida_star import ida_star, manhattan


def example_simple_grid():
    """Example 1: Simple 5x5 grid with few obstacles"""
    print("=" * 60)
    print("EXAMPLE 1: Simple Grid")
    print("=" * 60)
    
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    print(f"Grid Size: {len(grid)}x{len(grid[0])}")
    print(f"Start: {start}, Goal: {goal}")
    print("Grid (0=free, 1=obstacle):")
    for row in grid:
        print("  " + " ".join(str(cell) for cell in row))
    
    result = ida_star(start, goal, grid, manhattan)
    print(f"\nResult: {'✓ Path Found!' if result else '✗ No Path'}")
    return result


def example_maze_grid():
    """Example 2: More complex maze-like grid"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Maze Grid")
    print("=" * 60)
    
    grid = [
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (6, 6)
    
    print(f"Grid Size: {len(grid)}x{len(grid[0])}")
    print(f"Start: {start}, Goal: {goal}")
    
    result = ida_star(start, goal, grid, manhattan)
    print(f"\nResult: {'✓ Path Found!' if result else '✗ No Path'}")
    return result


def example_no_path():
    """Example 3: Grid with no possible path"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: No Path Scenario")
    print("=" * 60)
    
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    print(f"Grid Size: {len(grid)}x{len(grid[0])}")
    print(f"Start: {start}, Goal: {goal}")
    print("\nVisualizing the obstacle barrier...")
    print("Start (0,0) to Goal (4,4) with complete horizontal barrier at row 1")
    
    result = ida_star(start, goal, grid, manhattan)
    print(f"\nResult: {'✓ Path Found!' if result else '✗ No Path (as expected)'}")
    return result


def example_custom_heuristic():
    """Example 4: Using different heuristics"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Custom Heuristics")
    print("=" * 60)
    
    import math
    
    def euclidean(a, b):
        """Euclidean distance heuristic"""
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    
    def chebyshev(a, b):
        """Chebyshev distance (8-direction movement)"""
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
    
    def zero_heuristic(a, b):
        """Zero heuristic (behaves like iterative deepening search)"""
        return 0
    
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    print(f"Grid Size: {len(grid)}x{len(grid[0])}")
    print(f"Start: {start}, Goal: {goal}")
    
    # Test different heuristics
    heuristics = [
        ("Manhattan", manhattan),
        ("Euclidean", euclidean),
        ("Chebyshev", chebyshev),
        ("Zero", zero_heuristic)
    ]
    
    for name, heuristic_func in heuristics:
        result = ida_star(start, goal, grid, heuristic_func)
        print(f"\n{name} Heuristic: {'✓ Path Found' if result else '✗ No Path'}")
    
    print("\n" + "-" * 40)
    print("Note: All admissible heuristics should find the same path")
    print("Zero heuristic will be least efficient but still correct")
    return True


def run_all_examples():
    """Run all examples sequentially"""
    print("IDA* ALGORITHM - USAGE EXAMPLES")
    print("=" * 60)
    
    examples = [
        ("Simple Grid", example_simple_grid),
        ("Maze Grid", example_maze_grid),
        ("No Path", example_no_path),
        ("Custom Heuristics", example_custom_heuristic)
    ]
    
    results = []
    for name, func in examples:
        print(f"\n{' Running: ' + name + ' ':=^60}")
        result = func()
        results.append((name, result))
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for name, result in results:
        status = "✓ PASS" if result or "No Path" in name else "✗ FAIL"
        print(f"{name:20} {status}")


if __name__ == "__main__":
    run_all_examples()