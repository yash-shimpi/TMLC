from tabgan.sampler import GANGenerator
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def GAN(df, columns, target):
    df = df[columns]

    df = df.fillna(df.median(numeric_only=True).round(1))
    
    CATEGORICAL_COLS = list(set(df.columns) - set(df._get_numeric_data().columns))
    le = preprocessing.LabelEncoder()
    for i in CATEGORICAL_COLS:
        df[i] = le.fit_transform(df[i].astype(str))
    
    # Split into training and test sets
    df_x_train, df_x_test, df_y_train, df_y_test = train_test_split(
        df.drop(target, axis=1),
        df[target],
        test_size=0.20,
        #shuffle=False,
        random_state=42,
    )

    # Create dataframe versions for tabular GAN
    df_x_test, df_y_test = df_x_test.reset_index(drop=True), \
    df_y_test.reset_index(drop=True)
    df_y_train = pd.DataFrame(df_y_train)
    df_y_test = pd.DataFrame(df_y_test)

    gen_x, gen_y = GANGenerator(gen_x_times=1.1, cat_cols=None,
            bot_filter_quantile=0.001, top_filter_quantile=0.999, \
                is_post_process=True,
            adversarial_model_params={
                "metrics": "rmse", "max_depth": 2, "max_bin": 100, 
                "learning_rate": 0.02, "random_state": \
                    42, "n_estimators": 500,
            }, pregeneration_frac=2, only_generated_data=False,\
            gan_params = {"batch_size": 500, "patience": 25, \
            "epochs" : 500,}).generate_data_pipe(df_x_train, df_y_train,\
            df_x_test, deep_copy=True, only_adversarial=False, \
            use_adversarial=True)

    # gen_x = le.inverse_transform(gen_x)
    targetdf = pd.DataFrame(gen_y)
    targetdf.columns = target
    # gen_x[target] = 
    gen_x = pd.concat([gen_x, targetdf], axis=1)
    # print(gen_x.shape)
    # print("HIIIII")
    # print(gen_x.shape)
    return gen_x


