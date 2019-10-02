# ian.heywood@physics.ox.ac.uk


import pickle

with open('project_info.p','rb') as f:
    project_info = pickle.load(f,encoding='latin1')
#project_info = pickle.load(open('project_info.p','rb'))


myms = project_info['master_ms']
bpcal = project_info['primary']
pcals = project_info['secondary']


clearstat()
clearstat()


flagdata(vis=myms,mode='tfcrop',datacolumn='corrected',field=bpcal[1])
for i in range(0,len(pcals)):
    pcal = pcals[i][1]
    flagdata(vis=myms,mode='tfcrop',datacolumn='corrected',field=pcal[1])


flagmanager(vis=myms,mode='save',versionname='tfcrop_cals_corr')


clearstat()
clearstat()
