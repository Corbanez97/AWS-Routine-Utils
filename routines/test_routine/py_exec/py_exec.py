import pandas as pd
from io import StringIO

print('This is running inside other module, and being executed because of a call.')
print('For compliance: Hello World (◕‿◕✿)')

def test():
    print('Test ok')

def main(bytes, mapper: dict) -> None:

    df = pd.read_csv(StringIO(str(bytes, 'utf-8')))

    df.rename(columns = mapper, inplace = True)

    return df.to_csv(index=False).encode()