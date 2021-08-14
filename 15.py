import timeit


def permute(path: list[str], path_dict: dict[str, None], index: int, cache: dict) -> None:
    if index == len(path) - 1 or ("".join(path[:]), index) in cache:
        return
    for i in range(index + 1, len(path)):
        path[i], path[index] = path[index], path[i]
        path_dict["".join(path[:])] = None
        cache[("".join(path[:]), index)] = None
        permute(path, path_dict, index + 1, cache)
        path[i], path[index] = path[index], path[i]


def lattice_paths(grid_length: int, grid_width: int) -> int:
    starting_path = []
    for i in range(grid_length):
        starting_path.append('R')
        starting_path.append('D')
    path_dict = {"".join(starting_path): None}
    permute(starting_path, path_dict, 0, {})
    return len(list(path_dict.keys()))


start = timeit.default_timer()
print(lattice_paths(20, 20))
end = (timeit.default_timer() - start) * 1000.0
print(f"{end} ms")
