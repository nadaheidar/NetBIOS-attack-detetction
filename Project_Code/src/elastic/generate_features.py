import json
import logging
import time
import utils.url_utils as url_utils
import utils.url_analysis as url_analysis

def build_features(df, csv):
    """
    returns a dataframe with all the columns created and populated

    Args:
        df: A dataframe
        csv: A boolean. If True, the df data will be written to a csv file

    Returns:
        A dataframe.
    """

    for url in df["url"]:
        df["url_delimiter_count"] = df["url"].map(lambda x: url_utils.get_delimiter_count(x))
        df["url_digit_count"] = df["url"].map(lambda x: url_utils.get_digit_count(x))
        df["url_letter_count"] = df["url"].map(lambda x: url_utils.get_letter_count(x))
        df["url_symbol_count"] = df["url"].map(lambda x: url_utils.get_symbol_count(x))
        df["url_digit_to_letter_ratio"] = df["url"].map(lambda x: url_utils.get_digit_to_letter_ratio(x))
        df["url_encodes_characters"] = df["url"].map(lambda x: url_analysis.encodes_characters(x))
        df["url_uses_https"] = df["url"].map(lambda x: url_analysis.uses_https(x))
        df["url_get_port"] = df["url"].map(lambda x: url_analysis.get_port(x))
        df["url_uses_default_port_number"] = df["url"].map(lambda x: url_analysis.uses_default_port_number(x))
        df["ip_in_url"] = df["url"].map(lambda x: url_analysis.ip_in_url(x))

        break
    if csv:
        df.to_csv("sample_a2\\data\\features.csv", index=False)
    return df
