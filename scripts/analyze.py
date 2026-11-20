import pandas as pd, glob, numpy as np, io, csv
fr=[]
for f in sorted(glob.glob('hires/h*.csv')):
    try: fr.append(pd.read_csv(f, on_bad_lines='warn', engine='python'))
    except Exception as e: print('ERR',f,e)
h=pd.concat(fr,ignore_index=True)
# round-2 ads were all round-1 'none'; drop round-1 rows for them
h['_r2']=False
r1=[pd.read_csv(f,engine='python',on_bad_lines='warn') for f in sorted(glob.glob('hires/h[0-9].csv'))]
r2=[pd.read_csv(f,engine='python',on_bad_lines='warn') for f in sorted(glob.glob('hires/h_r*.csv'))]
r1=pd.concat(r1,ignore_index=True); r2=pd.concat(r2,ignore_index=True)
r1=r1[~r1.ad_id.isin(set(r2.ad_id))]
h=pd.concat([r1,r2],ignore_index=True)
h['subfield']=h.subfield.astype(str).str.split(' (',regex=False).str[0].str.strip()
h['subfield']=h.subfield.replace({'political_economy':'comparative/PE','comparative':'comparative/PE','comparative/methods':'comparative/PE','european_politics':'comparative/PE','political_communication':'american','public_policy_admin':'policy/other','other':'policy/other'})
h=h.drop_duplicates(subset=['ad_id','hire_name']).reset_index(drop=True)
ads=pd.read_csv('eligible.csv')
h=h.merge(ads[['ad_id','date','list','track']],on='ad_id',how='left')
def region(c):
    c=str(c)
    if c in('USA','United States','US'): return 'US'
    if c=='Canada': return 'Canada'
    if c in('UK','United Kingdom','Ireland'): return 'UK/Ireland'
    if c in('Germany','Switzerland','Austria','Netherlands','France','Spain','Italy','Norway','Denmark','Sweden','Belgium','Finland','Portugal','Turkey','Greece','Poland','Hungary','Czech Republic','Luxembourg'): return 'Continental Europe'
    if c in('Taiwan','China','Hong Kong','Japan','Singapore','South Korea','Korea','UAE','Qatar','Israel','India'): return 'Asia/Middle East'
    return 'Other'
h['region']=h.country.map(region)
def rk(r):
    r=str(r).lower()
    if any(k in r for k in['full','w3','chair','endowed','director']) and 'assistant' not in r: return 'senior'
    if 'associate' in r and 'assistant' not in r: return 'senior'
    if 'open' in r: return 'open'
    return 'junior'
h['rank_grp']=h.rank_advertised.map(rk)
num=['years_post_phd','n_postdocs','pubs_total_peer_reviewed','pubs_first_or_solo','pubs_top','books']
for c in num: h[c]=pd.to_numeric(h[c],errors='coerce')
h.to_csv('hires_merged.csv',index=False)
import sys
CONF=['high','medium','low'] if 'low' in sys.argv else ['high','medium']
id_=h[h.hire_name.notna()&(h.hire_name.astype(str).str.strip()!='')&h.confidence.isin(CONF)]
id_.to_csv('hires_identified.csv',index=False)
print('ads traced',ads.shape[0],'| rows',len(h),'| ads with a hire (hi/med):',id_.ad_id.nunique(),'| hires:',len(id_))
print(h.confidence.value_counts(dropna=False))
def summ(g):
    return pd.Series({'n':len(g),
      'pubs_med':g.pubs_total_peer_reviewed.median(),'pubs_p25':g.pubs_total_peer_reviewed.quantile(.25),'pubs_p75':g.pubs_total_peer_reviewed.quantile(.75),
      'top_med':g.pubs_top.median(),'share_any_top':(g.pubs_top>0).mean(),
      'solo1st_med':g.pubs_first_or_solo.median(),
      'yrs_postphd_med':g.years_post_phd.median(),'share_postdoc':(g.n_postdocs>0).mean(),
      'share_ABD_or_0':(g.years_post_phd<=0).mean()})
jr=id_[id_.rank_grp!='senior']
for k in ['rank_grp']: print(id_.groupby(k).apply(summ).round(2).to_string())
print('\nJUNIOR/OPEN by region'); print(jr.groupby('region').apply(summ).round(2).to_string())
print('\nJUNIOR/OPEN by subfield'); print(jr.groupby('subfield').apply(summ).round(2).to_string())
jr2=jr.copy(); jr2['yr']=pd.to_numeric(jr2.start_year,errors='coerce')
print('\nJUNIOR/OPEN by start year'); print(jr2.groupby('yr').apply(summ).round(2).to_string())
print('\nJUNIOR overall'); print(summ(jr).round(2).to_string())
