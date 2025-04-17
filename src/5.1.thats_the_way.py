import os

def thats_the_way(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise NotADirectoryError("Path is not a directory")
        return [f for f in os.listdir(directory_path) if f.startswith("deep")]
    except Exception as e:
        raise e

if __name__ == '__main__':
    print(thats_the_way("images"))
