def wearable_subset(df, pic_df):
    wearable_list = ['Apparel', 'Accessories', 'Footwear']
    wearable_df = df[df['masterCategory'].isin(wearable_list)]

    wearable_img = pic_df[ wearable_df.index.values ].copy()
    return (wearable_df, wearable_img)

def top2_subset(df, pic_df):
    list1 = ['Apparel', 'Accessories']
    top2_df = df[df['masterCategory'].isin(list1)]

    top2_img = pic_df[ top2_df.index.values ].copy()
    return (top2_df, top2_img)

def apparel_subset(df, pic_df):
    apparel_df = df[df['masterCategory']=='Apparel']
    apparel_img = pic_df[ apparel_df.index.values ].copy()
    return (apparel_df, apparel_img)

def accessory_subset(df, pic_df):
    accessory_df = df[df['masterCategory']=='Accessories']
    accessory_img = pic_df[ accessory_df.index.values ].copy()
    return (accessory_df, accessory_img)

def shoe_subset(df, pic_df):
    shoe_df = df[df['masterCategory']=='Footwear']
    shoe_img = pic_df[ shoe_df.index.values ].copy()
    return (shoe_df, shoe_img)
