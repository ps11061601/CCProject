import pandas as pd
from sklearn.preprocessing import StandardScaler
# Functions for use in Main.py


def scale(payload):
    #LOG.info("Scaling Payload: {payload}")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict


def create_dataframe(form):
    df_init = pd.DataFrame(
        columns=[
            'neighbourhood_group',
            'neighbourhood',
            'room_type',
            'number_of_reviews',
            'reviews_per_month',
            'availability_365'
        ]
    )

    df_input = df_init.append(
        {
            'neighbourhood_group': form.neighbourhood_group.data,
            'neighbourhood': form.neighbourhood.data,
            'room_type': form.room_type.data,
            'number_of_reviews': form.number_of_reviews.data,
            'reviews_per_month': form.reviews_per_month.data,
            'availability_365': form.availability_365.data,
        },
        ignore_index=True
    )

    return df_input
