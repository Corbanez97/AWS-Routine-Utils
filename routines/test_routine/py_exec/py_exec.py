import pandas as pd

print('This is running inside other module, and being executed because of a call.')
print('For compliance: Hello World (◕‿◕✿)')

def test():
    print('Test ok')

def main(parent: str, dump: str, mapper: dict) -> None:

    df = pd.read_csv(parent)

    df.rename(columns = mapper, inplace = True)

    df.to_csv(dump, index = False)