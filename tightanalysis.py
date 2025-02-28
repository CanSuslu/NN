from telnetlib import SE
import uproot3 as ur
import matplotlib.pyplot as plt
import pandas 
import numpy as np
import json


##LOAD THE JSON FILES. 

with open('/cephfs/user/suslu/jsonfiles/NT.json', 'r') as fp:
    NT = json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/Rp.json', 'r') as fp:
    Rp=json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/EpsHat3.json', 'r') as fp: 
    EpsHat3=json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/EpsHat234.json', 'r') as fp:
    EpsHat234=json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/Ra.json', 'r') as fp:
    Ra=json.load(fp)
with open('/cephfs/user/suslu/sg_jsonfiles/fp.json', 'r') as fp:
    f_p=json.load(fp)
with open('/cephfs/user/suslu/sg_jsonfiles/fa.json', 'r') as fp:
    fa=json.load(fp)
with open('/cephfs/user/suslu/sg_jsonfiles/sEpsHat3.json', 'r') as fp:
    sEpsHat3=json.load(fp)
with open('/cephfs/user/suslu/sg_jsonfiles/sEpsHat234.json', 'r') as fp:
    sEpsHat234=json.load(fp)
with open('/cephfs/user/suslu/sg_jsonfiles/Ns.json', 'r') as fp:
    NS = json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/EpsHatID.json', 'r') as fp:
    EpsHatID=json.load(fp)
with open('/cephfs/user/suslu/sg_jsonfiles/sEpsHatID.json', 'r') as fp:
    sEpsHatID=json.load(fp)
with open('/cephfs/user/suslu/sg_jsonfiles/sEpsHat.json', 'r') as fp:
    sEpsHat=json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/EpsHat.json', 'r') as fp:
    EpsHat=json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/NT_ID.json', 'r') as fp:
    NT_ID=json.load(fp)
with open('/cephfs/user/suslu/jsonfiles/DeltabEpsHat1234.json', 'r') as fp:
    DeltabEpsHat1234=json.load(fp)    
with open('/cephfs/user/suslu/jsonfiles/DeltabEpsHatID.json', 'r') as fp:
    DeltabEpsHatID=json.load(fp)    

#convert lists into arrays, for easier manipulation.

dicts=[NT,NS,Rp,EpsHat234,EpsHat3,Ra,fa, f_p,sEpsHat234,sEpsHat3,EpsHatID,sEpsHatID,sEpsHat,EpsHat,NT_ID,DeltabEpsHat1234,DeltabEpsHatID]

for i in range(len(dicts)):
    dicttt=dicts[i]
    dicttt["eta1"]=np.asarray(dicttt["eta1"])
    dicttt["eta2"]=np.asarray(dicttt["eta2"])
    dicttt["eta3"]=np.asarray(dicttt["eta3"])
    dicttt["eta4"]=np.asarray(dicttt["eta4"])

rows=["eta1","eta2","eta3","eta4"]

## EMPTY DICTIONARIES.

bEpsHat={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
bEpsHatID={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}

a={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
b={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
c={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}

## EQUATION 22-24.

for i in range(len(rows)):
    a[rows[i]]=Rp[rows[i]] - f_p[rows[i]]
    b[rows[i]]=(Rp[rows[i]] * (sEpsHat[rows[i]] + EpsHat3[rows[i]])) - (f_p[rows[i]] * (EpsHat[rows[i]] + sEpsHat3[rows[i]]))
    c[rows[i]]=(Rp[rows[i]] * EpsHat3[rows[i]] * sEpsHat[rows[i]]) - (f_p[rows[i]] * sEpsHat3[rows[i]] * EpsHat[rows[i]])

for i in range(len(rows)):
    bEpsHatID[rows[i]] = ((b[rows[i]] + np.sqrt((b[rows[i]])**2 -4*a[rows[i]]*c[rows[i]])) )/(2*a[rows[i]])

for i in range(len(rows)):
    a[rows[i]]=Ra[rows[i]] - fa[rows[i]]
    b[rows[i]]=(Ra[rows[i]] * (sEpsHat[rows[i]] + EpsHat234[rows[i]])) - (fa[rows[i]] * (EpsHat[rows[i]] + sEpsHat234[rows[i]]))
    c[rows[i]]=(Ra[rows[i]] * EpsHat234[rows[i]] * sEpsHat[rows[i]]) - (fa[rows[i]] * sEpsHat234[rows[i]] * EpsHat[rows[i]])

for i in range(len(rows)):
    bEpsHat[rows[i]] = (((b[rows[i]]) + np.sqrt((b[rows[i]])**2 -4*a[rows[i]]*c[rows[i]]) )/(2*a[rows[i]]))

EpsTightID={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}

#for i in range(len(rows)):
#    EpsTightID[rows[i]] = (((EpsHatID[rows[i]]-bEpsHatID[rows[i]])/(sEpsHatID[rows[i]]-bEpsHatID[rows[i]]))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-bEpsHat[rows[i]])/(sEpsHat[rows[i]]-bEpsHat[rows[i]]))*NT[rows[i]])

#print(EpsTightID)

plt.plot(sEpsHatID["eta1"], marker=".", label="$\hat{\epsilon}^s_{I}$")
plt.plot(EpsHatID["eta1"], marker=".", label="$\hat{\epsilon}_{ID}$")
plt.plot(bEpsHatID["eta1"], marker=".", label="$\hat{\epsilon}^b_{ID}$")
plt.ylabel("track isolation efficiency")
plt.xlabel("pT bins")
plt.title("  0<eta<0.6  ")
plt.legend()
plt.savefig("eta1EpsIDnewcut.pdf")
plt.show()
plt.close()
#plt.plot(EpsTightID["eta1"], marker=".", label="$\hat{\epsilon}^s_{I}$")
#plt.ylabel("track isolation efficiency")
#plt.xlabel("pT bins")
#plt.title("  0<eta<0.6  ")
#plt.legend()
#plt.savefig("tightIDnew.pdf")
#plt.show()



EpsTightID1={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID2={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID3={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID4={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
for i in range(len(rows)):
    EpsTightID[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]])))*NT[rows[i]])
    EpsTightID1[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
    EpsTightID2[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
    EpsTightID3[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
    EpsTightID4[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
plt.plot(EpsTightID1["eta1"],label="1")
plt.plot(EpsTightID2["eta1"],label="2")
plt.plot(EpsTightID3["eta1"],label="3")
plt.plot(EpsTightID4["eta1"],label="4")
plt.plot(EpsTightID["eta1"],label="nom")
plt.legend()
plt.savefig("tightID.pdf")
plt.show()

�����������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������snewcut4.pdf")
#plt.show()
plt.close()
#plt.plot(EpsTightID["eta1"], marker=".", label="$\hat{\epsilon}^s_{I}$")
#plt.ylabel("track isolation efficiency")
#plt.xlabel("pT bins")
#plt.title("  0<eta<0.6  ")
#plt.legend()
#plt.savefig("tightIDnew.pdf")
#plt.show()



EpsTightID1={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID2={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID3={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID4={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
EpsTightID={key:np.array([]) for  key in ["eta1","eta2","eta3","eta4"]}
for i in range(len(rows)):
    EpsTightID[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]])))*NT[rows[i]])
    EpsTightID1[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
    EpsTightID2[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]+DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
    EpsTightID3[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]+DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
    EpsTightID4[rows[i]] = (((EpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]]))/(sEpsHatID[rows[i]]-(bEpsHatID[rows[i]]-DeltabEpsHatID[rows[i]])))*NT_ID[rows[i]])/(((EpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]]))/(sEpsHat[rows[i]]-(bEpsHat[rows[i]]-DeltabEpsHat1234[rows[i]])))*NT[rows[i]])
#plt.plot(EpsTightID1["eta1"],label="1")
#plt.plot(EpsTightID2["eta1"],label="2")
#plt.plot(EpsTightID3["eta1"],label="3")
#plt.plot(EpsTightID4["eta1"],label="4")
plt.plot(x,EpsTightID["eta1"],marker="o",label="nominal")
plt.xlabel("photon $E_T$ [GeV]")
plt.ylabel("Tight-ID Efficiency")
plt.text(150,0.6, "$1.81 \leq |\eta| < 2.37$")
plt.legend()
plt.xscale('log')
plt.savefig("tightID.pdf")
plt.show()

