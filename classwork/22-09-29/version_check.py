def version_bigger_than(v):
    with open("classwork/requirements.txt") as file:
        results = []
        for line in file.readlines():
            version = line.split("==")[-1]
            version = float(".".join(version.split(".")[:2]))
            if version >= v:
                results.append("".join(line.split("==")[:-1]))
        return results


print(version_bigger_than(3.0))
