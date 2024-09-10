"""    
Author: Zachary Flohr    
Date: 2024-09-10
"""    

def legoBlocks(n: int, m: int) -> int:
    """Compute the number of combinations a wall may be built.

    Args:
        n: The height of the wall.
        m: The width of the wall.

    Returns:
        The number of combinations a wall of height n and width m may
        be built from lego blocks while ensuring that 1) the wall
        doesn't have any holes in it, 2) the wall doesn't have a
        straight vertical break across all rows of bricks, and 3) the
        bricks are laid horizontally.
    """
    mod = 10 ** 9 + 7
    block_widths = [1, 2, 3, 4]
    width_combinations = [0] * (m + 1)
    width_combinations[0] = 1
    total_wall_combinations = [0] * (m + 1)
    valid_wall_combinations = [0] * (m + 1)
    for wall_width in range(1, m + 1):
        for block_width in block_widths:
            if wall_width >= block_width:
                width_combinations[wall_width] += (
                    width_combinations[wall_width - block_width] % mod)
    for width in range(1, m + 1):
        total_wall_combinations[width] = pow(width_combinations[width], n, mod)
        valid_wall_combinations[width] = total_wall_combinations[width]
        for split in range(1, width):
            valid_wall_combinations[width] -= (
                ((valid_wall_combinations[split]
                * total_wall_combinations[width - split]) + mod) % mod)
    return valid_wall_combinations[m] % mod

