import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def get_random_dataframe(n_rows: int, m_cols: int) -> pd.DataFrame:
    """
    Creates a dataframe of size n_rows x m_cols with random values

    Args:
        n_rows: number of rows
        m_cols: number of columns

    Return:
        dataframe of size n_rows x m_cols with random values
    """

    df = pd.DataFrame(np.random.rand(n_rows, m_cols))

    return df


def main():
    df = get_random_dataframe(10, 4)

    print(df)

    df.plot.area()
    plt.show()


if __name__ == "__main__":
    main()
