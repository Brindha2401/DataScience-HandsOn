import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_data(path):
    df = pd.read_csv(path)
    print("Data loaded successfully!")
    return df


def explore_data(df):
    print("\nData Overview:")
    print(df.head())
    print("\nData Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData Info:")
    print(df.info())
    print("\nStatistical Summary:")
    print(df.describe())


def clean_data(df):
    print("\nCleaning Data:")
    df = df.drop(columns=['famsize'], errors='ignore')

    df['age'] = df['age'].fillna(df['age'].mean())

    print("\nMissing values handled.")
    return df


def filter_sort_data(df):
    print("\nFilter Students older than 18")
    print(df[df['age'] > 18][['school', 'age']])

    print("\nSorted by Health:")
    print(df.sort_values(by='health', ascending=False).head())


def group_aggregate_data(df):
    print("\nGrouping: Average StudyTime")
    print(df.groupby('Pstatus')['studytime'].mean())


def encode_data(df):
    print("\nEncoding categorical columns:")
    label_enc = LabelEncoder()
    df['sex'] = label_enc.fit_transform(df['sex'])
    print("Encoding complete.")
    return df


def scale_data(df):
    print("\nScaling numerical data:")
    scaler = StandardScaler()
    numeric_cols = ['G1', 'G2', 'G3']
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print("Scaling complete.")
    return df


def sample_data(df):
    print("\nSampling the data:")
    sample = df.sample(n=10, random_state=1)
    print(sample)
    return sample


def main():
    path = "Math-Students.csv"
    df = load_data(path)
    explore_data(df)
    df = clean_data(df)
    filter_sort_data(df)
    group_aggregate_data(df)
    df = encode_data(df)
    df = scale_data(df)
    sample_data(df)


if __name__ == "__main__":
    main()
