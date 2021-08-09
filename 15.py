

def permute(path: list[str], path_dict: dict[str, None], index: int) -> None:
    if index == len(path):
        path_dict["".join(path[:])] = None
    for i in range(index, len(path)):
        path[i], path[index] = path[index], path[i]
        permute(path, path_dict, index + 1)
        path[i], path[index] = path[index], path[i]


def lattice_paths(grid_length: int, grid_width: int) -> int:
    starting_path = []
    for i in range(grid_length):
        starting_path.append('R')
        starting_path.append('D')
    path_dict = {}
    permute(starting_path, path_dict, 0)
    return len(list(path_dict.keys()))


print(lattice_paths(20, 20))
