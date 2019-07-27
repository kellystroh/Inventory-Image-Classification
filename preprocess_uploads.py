all_img = []
for i, ix in enumerate( df.id ):
    if i%2000==0:
        print(i, len(df))

    fn = r'data/data/images/{}.jpg'.format(ix)
    try:
        img = imageio.imread(fn)
        if img.shape!=(80, 60, 3):
            all_img.append( [0]*(60*80*3) )
        else:
            all_img.append( img.ravel() )
    except FileNotFoundError:
        all_img.append( [0]*(60*80*3) )

all_img = np.stack(all_img)
bw_float64 = all_img.reshape(-1, 80, 60, 3).mean(3).reshape(-1, 80*60)
bw_img = bw_float64.astype('float16')