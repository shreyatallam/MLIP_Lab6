import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(feature_target_sample):
    return_tuple = data_split(*feature_target_sample)
    # TODO test if the length of return_tuple is 4
    # Test if the length of return_tuple is 4
    assert len(return_tuple) == 4

    # Test if the first two elements are dataframes (train and test features)
    assert isinstance(return_tuple[0], pd.DataFrame)  # Train features
    assert isinstance(return_tuple[1], pd.DataFrame)  # Test features

    # Test if the last two elements are series (train and test targets)
    assert isinstance(return_tuple[2], pd.Series)  # Train target
    assert isinstance(return_tuple[3], pd.Series)  # Test target

    # Test if the split was done properly by comparing the sizes
    train_size = return_tuple[0].shape[0]  # Number of rows in train features
    test_size = return_tuple[1].shape[0]   # Number of rows in test features
    total_size = feature_target_sample[0].shape[0]  # Total number of rows in the original dataset

    # Assert the sum of train and test sizes equals the total size
    assert train_size + test_size == total_size
