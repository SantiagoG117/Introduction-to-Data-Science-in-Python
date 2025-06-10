import pandas as pd
import numpy as np
import scipy.stats as stats

# Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the following education levels:
#   - equal to less than high school (<12)
#   - high school (12)
#   - more than high school but not a college graduate (>12)
#   - and college degree.


# Read the file
df = pd.read_csv('./datasets/NISPUF17.csv', index_col=0)


def proportion_of_education():

    # Rename required columns:
    df.rename(columns={'EDUC1': 'Education of the Mother'}, inplace=True)

    # Define the dictionary keys
    keys = ['less than high school', 'high school',
            'more than high school but not college', 'college']
    dictionary = dict.fromkeys(keys)

    # Get the unique categorical values for education_levels
    education_levels = sorted(df['Education of the Mother'].unique().tolist())

    # Get the proportion for each education level of the mother and add it to the dictionary in the respective key
    for education_level in education_levels:
        key = keys[education_level - 1]
        result_set = df[df['Education of the Mother']
                        == education_level]
        proportion = (len(result_set) / len(df))
        dictionary[key] = proportion

    return dictionary


# Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not
# The function should result a touple in the form of (#.# , #.#). The first for yes and the second for no

def avg_influenza_doses():
    # //? Create a local copy of the DataFrame with the required columns
    local_df = df.rename(columns={'CBF_01': 'Baby was breastfed',
                                            'P_NUMFLU': 'Number of seasonal influenza doses'})

    # //? Remove unnecesary data and drop rows with NaN
    local_df = local_df[~local_df['Baby was breastfed'].isin([77, 99])].dropna(
        subset=['Number of seasonal influenza doses'])

    avg_breastfed = float(local_df['Number of seasonal influenza doses'].where(
        local_df['Baby was breastfed'] == 1).mean())

    avg_not_breastfed = float(local_df['Number of seasonal influenza doses'].where(
        local_df['Baby was breastfed'] == 2).mean())

    return (avg_breastfed, avg_not_breastfed)


# Determine the relation between the effectiveness of a chickenpox vaccine and the sex of the child
# Calulate the ratio of:
# Number of children who contracted chickenpox and got at least one dose of varicella VS Number of children who did not contracted chickenpox and got at least one dose of varicella

def chickenpox_by_sex():
    # //? Create a local copy of the DataFrame with the required columns renamed
    local_df = df.rename(columns={
        'HAD_CPOX': 'Had Chickenpox',
        'P_NUMVRC': 'Varicella doses'
    })

    # //? Clean the data, remove unnecessary values, and drop rows with NaN
    local_df = local_df[~local_df['Had Chickenpox'].isin(
        [77, 99])].dropna(subset='Varicella doses')

    # //? Undertake calculations
    # Boolean Masks
    mask_had_chickenpox_and_vaccinated = (local_df['Had Chickenpox'] == 1) & (
        local_df['Varicella doses'] >= 1)

    mask_no_chickenpox_and_vaccinated = (local_df['Had Chickenpox'] == 2) & (
        local_df['Varicella doses'] >= 1)

    # Filtered values
    male_had_chickenpox_and_vaccinated = local_df['SEX'].where(
        (mask_had_chickenpox_and_vaccinated) & (local_df['SEX'] == 1)).sum()

    male_no_chickenpox_and_vaccinated = local_df['SEX'].where(
        (mask_no_chickenpox_and_vaccinated) & (local_df['SEX'] == 1)).sum()

    female_had_chickenpox_and_vaccinated = local_df['SEX'].where(
        (mask_had_chickenpox_and_vaccinated) & (local_df['SEX'] == 2)).sum()

    female_no_chickenpox_and_vaccinated = local_df['SEX'].where(
        (mask_no_chickenpox_and_vaccinated) & (local_df['SEX'] == 2)).sum()

    # Ratios:
    ratio_for_male = float(male_had_chickenpox_and_vaccinated /
                           male_no_chickenpox_and_vaccinated)
    ratio_for_female = float(female_had_chickenpox_and_vaccinated /
                             female_no_chickenpox_and_vaccinated)

    return {"male": ratio_for_male, "female": ratio_for_female}


# Determine the correlation between having the chickenpox and the number of chickenpox doses given
def corr_chickenpox():
    # //? Create a local copy of the DataFrame with the required columns renamed
    local_df = df.rename(columns={
        'HAD_CPOX': 'Had Chickenpox',
        'P_NUMVRC': 'Varicella doses'
    })

    # //? Clean the data, remove unnecessary values, and drop rows with NaN
    local_df = local_df[~local_df['Had Chickenpox'].isin(
        [77, 99])].dropna(subset='Varicella doses')

    r, pval = stats.pearsonr(
        local_df['Had Chickenpox'], local_df['Varicella doses'])

    return r


print(corr_chickenpox())
