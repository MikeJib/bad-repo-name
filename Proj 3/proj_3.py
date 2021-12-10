import pandas as pd
# # # p_3 input
data = open("p3_input.txt", "r").read().splitlines()
ox_df = pd.DataFrame(data)
cd_df = pd.DataFrame(data)

# # # p_3 part 1
most_common = ""
least_common = ""

ox_df = ox_df[0].apply(lambda x: pd.Series(list(x)))
cd_df = cd_df[0].apply(lambda x: pd.Series(list(x)))
for i in range(len(ox_df.columns)):
    most_common += str(ox_df[i].value_counts().idxmax())
    least_common += str(ox_df[i].value_counts().idxmin())

print(int(most_common) * int(least_common))

# # # p_3 part 2
ox_filtered = ""
cd_filtered = ""
is_equal = False

for i in range(len(ox_df.columns)):
    ox_df[i].astype(int)
    num_count = ox_df[i].value_counts().sort_index(ascending=True)
    if ox_df[i].value_counts()[0] == ox_df[i].value_counts()[1]:
        is_equal = True

    if num_count[1] >= num_count[0] or is_equal:
        ox_df = ox_df[ox_df[i].str.startswith("1")]
    else:
        ox_df = ox_df[ox_df[i].str.startswith("0")]
    is_equal = False
    print(ox_df)

for i in range(len(cd_df.columns)):
    cd_df[i].astype(int)
    num_count = cd_df[i].value_counts().sort_index(ascending=True)
    try:
        if cd_df[i].value_counts()[0] == cd_df[i].value_counts()[1]:
            is_equal = True

        if num_count[1] >= num_count[0] or is_equal:
            cd_df = cd_df[cd_df[i].str.startswith("0")]
        else:
            cd_df = cd_df[cd_df[i].str.startswith("1")]
    except:
        pass
    is_equal = False

for i in range(len(ox_df.columns)):
    ox_filtered += str(ox_df.iloc[0][i])
    cd_filtered += str(cd_df.iloc[0][i])

print(ox_filtered)
print(cd_filtered)

print(int(ox_filtered, 2) * int(cd_filtered, 2))