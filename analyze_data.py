import pandas as pd


def main():
    df_expression = pd.read_csv(
        'train_data\\train_expression.csv.gz', compression='gzip')

    print(df_expression)


if __name__ == '__main__':
    main()
