class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = 0
        litter_id = {}
        litter_count = 0

        # find S and assign each L a bit number
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1
        
        # required by the problem statement
        lumetarkon = (classroom, energy)

        full_mask = (1 << litter_count) - 1

        # No litter
        if full_mask == 0:
            return 0

        # (row, col, remaining_energy, mask, moves)
        queue = deque([
            (start_r, start_c, energy, 0, 0)
        ])

        visited = {
            (start_r, start_c, energy, 0)
        }

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()

            # Collected everything
            if mask == full_mask:
                return moves

            # Cannot move anymore
            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Obstacle
                if classroom[nr][nc] == "X":
                    continue

                # Moving costs 1 energy
                new_energy = curr_energy - 1

                # Reset energy
                if classroom[nr][nc] == "R":
                    new_energy = energy

                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == "L":
                    index = litter_id[(nr, nc)]
                    new_mask |= 1 << index

                state = (nr, nc, new_energy, new_mask)

                if state in visited:
                    continue

                visited.add(state)

                queue.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1