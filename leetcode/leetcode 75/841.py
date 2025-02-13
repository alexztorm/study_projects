def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    visited = [False] * len(rooms)
    stack = [0]

    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True

            for key in rooms[current]:
                stack.append(key)

    return True if all(visited) else False


if __name__ == '__main__':
    print(canVisitAllRooms([[1], [2], [3], []]))
    print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
