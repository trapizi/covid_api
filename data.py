import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

def get_json_reponse(file_name: str) -> dict:
    json_output = []
    df = cleanse_data(file_name)
    count_df, lga_test_df = process_data(df)[0], process_data(df)[1]

    for _, row in count_df.iterrows():
        lga_code = row['lga_code19']
        lga_name = row['lga_name19']
        lga_total_test_count = row['count']
        # Get df of current lga's test count for each test dates
        curr_lga_df = lga_test_df.loc[lga_test_df['lga_code19'] == lga_code]
        
        json_output.append({
            'lga_code': lga_code,
            'lga_name': lga_name,
            'count': lga_total_test_count,
            'greatest': {
                'count': get_day_with_most_test(curr_lga_df)[0],
                'date': get_day_with_most_test(curr_lga_df)[1]
            },
            'least': {
                'count': get_day_with_least_test(curr_lga_df)[0],
                'date': get_day_with_least_test(curr_lga_df)[1]
            },
        })

    return json_output


def process_data(df: pd.DataFrame):

    # lga_count DataFrame
    lga_count_df = df.groupby(['lga_code19', 'lga_name19']).size().to_frame('count').reset_index()
    lga_count_df = lga_count_df.sort_values(by=['count'], ascending=False)

    # Test date count group by lga ans test date DataFrame
    test_date_count_df = df.groupby(['lga_code19','test_date']).size().to_frame('count').reset_index()
 
    return lga_count_df, test_date_count_df


def cleanse_data(file_name: str) -> pd.DataFrame: 
    df = pd.read_csv(file_name)
    
    # Filter records with null value in lga_code19, lga_name_19
    vector_not_null = df['lga_code19'].notnull()

    df_not_null = df[vector_not_null]
    df_not_null.lga_code19 = df_not_null.lga_code19.astype(int)

    # Drop unwanted columns
    df_not_null = df_not_null.drop(columns=['lhd_2010_code','lhd_2010_name'])
    return df_not_null


def get_day_with_most_test(input_df: pd.DataFrame):
    df = input_df.loc[input_df['count'].idxmax()]
    return int(df['count']), df['test_date']


def get_day_with_least_test(input_df: pd.DataFrame):
    df = input_df.loc[input_df['count'].idxmin()]
    return int(df['count']), df['test_date']
