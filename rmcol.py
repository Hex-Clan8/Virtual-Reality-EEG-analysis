# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:52:39 2021

@author: PC
"""
import pandas


def Remove_Colinearity(df1,df2):
    
    column_titles = df1.columns
    column_titles_to_remove = []
    column_index = 0
    for index, row in df2.iterrows():
        if column_index == len(column_titles):
            break
        if column_titles[column_index] in column_titles_to_remove:
            column_index += 1
            continue
        inner_index = column_index + 1
        for corr in row[inner_index:]:
            if corr < -0.9 or corr > 0.9:
                if column_titles[inner_index] not in column_titles_to_remove:
                    column_titles_to_remove.append(column_titles[inner_index])
            inner_index += 1;
        column_index += 1
    return df1.drop(columns=column_titles_to_remove,axis=1)