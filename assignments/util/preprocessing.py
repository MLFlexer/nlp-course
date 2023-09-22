from datasets import load_dataset
import pandas as pd

def get_preprocessed_data():
    dataset = load_dataset("copenlu/answerable_tydiqa")

    train_set = dataset["train"]
    validation_set = dataset["validation"]

    df_train = train_set.to_pandas()
    df_val = validation_set.to_pandas()

    df_train.head()


    # Get train and validation data for each language
    df_train_bengali = df_train[df_train['language'] == 'bengali']
    df_train_arabic = df_train[df_train['language'] == 'arabic']
    df_train_indonesian = df_train[df_train['language'] == 'indonesian']

    df_val_bengali = df_val[df_val['language'] == 'bengali']
    df_val_arabic = df_val[df_val['language'] == 'arabic']
    df_val_indonesian = df_val[df_val['language'] == 'indonesian']

    print(len(df_train_bengali))
    print(len(df_train_arabic))
    print(len(df_train_indonesian))

    # For testing
    df_val_english = df_val[df_val['language'] == 'english']
    df_train_english = df_train[df_train['language'] == 'english']

    df_train_bengali_document = df_train[df_train['language'] == 'bengali']["document_plaintext"]
    df_train_arab_document = df_train[df_train['language'] == 'arabic']["document_plaintext"]
    df_train_indonesian_document = df_train[df_train['language'] == 'indonesian']["document_plaintext"]
    df_train_indonesian_document.head()

    df_train_english_document = df_train[df_train['language'] == 'english']["document_plaintext"]
    return {"df_train": df_train,
            "df_val": df_val,
            "df_train_bengali": df_train_bengali,
            "df_train_arabic": df_train_arabic,
            "df_train_indonesian": df_train_indonesian,
            "df_val_bengali": df_val_bengali,
            "df_val_arabic": df_val_arabic,
            "df_val_indonesian": df_val_indonesian,
            "df_val_english": df_val_english,
            "df_train_english": df_train_english,
            "df_train_bengali_document": df_train_bengali_document,
            "df_train_arab_document": df_train_arab_document,
            "df_train_indonesian_document": df_train_indonesian_document,
            "df_train_english_document": df_train_english_document
                }

