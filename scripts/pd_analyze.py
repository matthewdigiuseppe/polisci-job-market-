import pandas as pd, glob, sys
h=pd.concat([pd.read_csv(f,engine='python',on_bad_lines='warn') for f in sorted(glob.glob('pd_hires/p*.csv'))],ignore_index=True)
h=h.drop_duplicates(subset=['ad_id','hire_name']).reset_index(drop=True)
h=h[~h.hire_name.astype(str).str.contains('Quiros|Nicholas Willis')]
cvf=sorted(glob.glob('pd_cv/c*.csv'))
if cvf:
    cv=pd.concat([pd.read_csv(f,engine='python',on_bad_lines='warn') for f in cvf],ignore_index=True).drop_duplicates(['ad_id','hire_name'],keep='last')
    h=h.merge(cv,on=['ad_id','hire_name'],how='left',suffixes=('','_cv'))
    for c in ['phd_institution','phd_country','phd_year','years_post_phd','prior_postdocs','pubs_total_peer_reviewed','pubs_first_or_solo','pubs_top','next_position','next_position_year','cv_source_url']:
        if c+'_cv' in h: h[c]=h[c+'_cv'].where(h[c+'_cv'].notna(),h[c]); h=h.drop(columns=c+'_cv')
    h=h.rename(columns={'notes_cv':'cv_notes'})
ads=pd.read_csv('pd_eligible.csv')
h=h.drop(columns=[c for c in ['type','subfield','country','institution'] if c in h]).merge(ads[['ad_id','date','list','type','subfield','country','institution']],on='ad_id',how='left')
def region(c):
    c=str(c)
    if c in('USA',): return 'US'
    if c in('UK','Ireland'): return 'UK/Ireland'
    if c in('Germany','Austria','Switzerland'): return 'DACH'
    if c in('Sweden','Denmark','Norway','Finland','Netherlands','Belgium'): return 'Nordic/Benelux'
    if c in('France','Spain','Italy','Portugal'): return 'Southern Europe/France'
    if c=='Canada': return 'Canada'
    return 'Other'
h['region']=h.country.map(region)
h['subfield']=h.subfield.replace({'political_economy':'comparative/PE','comparative':'comparative/PE','european_politics':'comparative/PE','political_communication':'american','public_policy_admin':'policy/other','other':'policy/other','political_theory':'policy/other'})
for c in ['years_post_phd','prior_postdocs','pubs_total_peer_reviewed','pubs_first_or_solo','pubs_top']: h[c]=pd.to_numeric(h[c],errors='coerce')
h['us_phd']=h.phd_country.astype(str).str.contains('US|United States',case=False)
np_=h.next_position.astype(str).str.lower()
h['next_tt']=np_.str.contains('asst|assistant prof|lecturer|associate prof|tenure|universitair docent|w1|juniorprof')
h['next_known']=h.next_position.notna()&~np_.str.contains('still|unknown|nan|current')
h.to_csv('pd_hires_merged.csv',index=False)
CONF=['high','medium','low'] if 'low' in sys.argv else ['high','medium']
d=h[h.hire_name.notna()&(h.hire_name.astype(str).str.strip()!='')&h.confidence.isin(CONF)]
d.to_csv('pd_hires_identified.csv',index=False)
print('ads',len(ads),'| ads w/ hire',d.ad_id.nunique(),'| hires',len(d)); print(h.confidence.value_counts(dropna=False).to_dict())
def s(g):
    return pd.Series({'n':len(g),'pubs_med':g.pubs_total_peer_reviewed.median(),'p25':g.pubs_total_peer_reviewed.quantile(.25),'p75':g.pubs_total_peer_reviewed.quantile(.75),
     'zero_pubs':(g.pubs_total_peer_reviewed==0).mean(),'any_top':(g.pubs_top>0).mean(),'yrs_med':g.years_post_phd.median(),'ABD_or_0':(g.years_post_phd<=0).mean(),
     'had_prior_pd':(g.prior_postdocs>0).mean(),'us_phd':g.us_phd.mean(),'next_tt|known':g[g.next_known].next_tt.mean(),'n_next_known':g.next_known.sum()})
print('\nOVERALL'); print(s(d).round(2).to_string())
for k in ['type','region','subfield']: print('\nBY',k); print(d.groupby(k).apply(s).round(2).to_string())
