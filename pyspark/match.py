import datetime
distance_cutoff = 250
time_diff = datetime.timedelta(seconds=30000)
import time
import nltk
nltk.download('punkt')
nltk.download('wordnet')
import tagnews

from geopy import distance as geo

def find_the_matching(newsdata,crimesdata,distance_cutoff,time_diff):
    tag = crimetags.tagtext(newsdata['bodytext'], prob_thresh=0.5)
    if tag == None:
        return pd.Series([newsdata['id'],np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    geostrings = geoextractor.extract_geostrings(newsdata['bodytext'], prob_thresh=0.5)
    coords, scores = geoextractor.lat_longs_from_geostring_lists(geostrings)
    if scores.shape[0]==0:
        return pd.Series([newsdata['id'],np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    lat = coords['lat'][0]
    long = coords['long'][0]
    matching_temp = crimesdata[ (newsdata['created']<=crimesdata['date']+ time_diff) 
                               & (crimesdata['date']<=newsdata['created']) & (lat<=crimesdata['lat']+0.05)
                               & (lat>=crimesdata['lat']-0.05) & (long<=crimesdata['long']+0.05) 
                               & (long>=crimesdata['long']-0.05) ]
    if matching_temp.count().sum()==0:
        return pd.Series([newsdata['id'],np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    idx = matching_temp.apply(lambda x: geo.distance((x['lat'],x['long']),(lat,long)).m,axis =1 ).idxmin()
    return_data = matching_temp.loc[idx]
    geo_dis = geo.distance((return_data['lat'],return_data['long']),(lat,long)).m
    if geo_dis > distance_cutoff:
        return pd.Series([newsdata['id'],np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan])
    print(newsdata.id,crimesdata.id,lat,lon)
    return pd.Series([newsdata['id'],tag[0],newsdata['created'],lat,long,return_data['id'],return_data['type'],return_data['date'],return_data['lat'],return_data['long']])
    
