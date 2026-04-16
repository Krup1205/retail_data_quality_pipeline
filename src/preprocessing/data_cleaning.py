def clean_data(df):

    df = df.copy()

    df['CompetitionDistance'] = df['CompetitionDistance'].fillna(
        df['CompetitionDistance'].median()
    )

    df['CompetitionOpenSinceMonth'] = df['CompetitionOpenSinceMonth'].fillna(0)
    df['CompetitionOpenSinceYear'] = df['CompetitionOpenSinceYear'].fillna(0)

    df.loc[df['Promo2'] == 0, ['Promo2SinceWeek', 'Promo2SinceYear', 'PromoInterval']] = [0, 0, 'None']

    df['Promo2SinceWeek'] = df['Promo2SinceWeek'].fillna(0)
    df['Promo2SinceYear'] = df['Promo2SinceYear'].fillna(0)
    df['PromoInterval'] = df['PromoInterval'].fillna('None')

    df = df[df['Open'] == 1].copy()

    return df