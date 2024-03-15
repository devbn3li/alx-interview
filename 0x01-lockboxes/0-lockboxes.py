def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a queue for BFS
    queue = [0]

    while queue:
        # Pop the first box from the queue
        current_box = queue.pop(0)
        # Mark the current box as visited
        visited.add(current_box)

        # Check all the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and that box has not been visited yet, add it to the queue
            if key < len(boxes) and key not in visited:
                queue.append(key)

    # If all boxes have been visited, return True, otherwise, return False
    return len(visited) == len(boxes)
