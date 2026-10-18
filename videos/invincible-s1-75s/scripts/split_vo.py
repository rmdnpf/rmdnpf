"""Split assets/vo/vo-full.wav into 01..10.wav: align sentence ends to detected silences (DP on syllable estimate)."""
import re, subprocess, sys
L=[l.split('|')[3].strip() for l in open('VO_SCRIPT.md') if re.match(r'\| `\d\d\.wav`',l)]
F='assets/vo/vo-full.wav'
T=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',F]))
out=subprocess.run(['ffmpeg','-hide_banner','-i',F,'-af','silencedetect=noise=-35dB:d=0.3','-f','null','-'],capture_output=True,text=True).stderr
st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)]
en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',out)]
sil=list(zip(st,en))
U=[]
for li,x in enumerate(L):
    ss=re.findall(r'[^.?]+[.?]',x)
    for si,s in enumerate(ss):
        U.append((len(re.findall(r'[aiueoAIUEO]',s))+0.8*s.count(',')+0.8*s.count(':'),2 if si==len(ss)-1 else 1,li,s.strip()[:30]))
tot=sum(u[0] for u in U);cum=0;pos=[]
for u in U: cum+=u[0];pos.append(cum/tot*T)
n=len(U);m=len(sil);mid=[(a+b)/2 for a,b in sil];dur=[b-a for a,b in sil];INF=1e9
cost=lambda i,j:(mid[j]-pos[i])**2/(2.0 if U[i][1]==2 else 1.0)-8*dur[j]
dp=[[INF]*m for _ in range(n-1)];bk=[[None]*m for _ in range(n-1)]
for j in range(m): dp[0][j]=cost(0,j)
for i in range(1,n-1):
    for j in range(i,m):
        for pj in range(i-1,j):
            c=dp[i-1][pj]+cost(i,j)
            if c<dp[i][j]: dp[i][j]=c;bk[i][j]=pj
j=min(range(n-2,m),key=lambda j:dp[n-2][j]);ch=[j]
for i in range(n-2,0,-1): j=bk[i][j];ch.append(j)
ch=ch[::-1]
for i,j in enumerate(ch): print(U[i][2]+1,U[i][1],U[i][3],'| exp',round(pos[i],1),'-> sil',round(mid[j],2),round(dur[j],2))
cuts=[0]+[round(mid[ch[i]],2) for i in range(n-1) if U[i][1]==2]+[T]
cuts=[0,10.33,17.56,24.25,33.83,47.15,54.70,61.17,70.09,77.38,T]  # manual override of lines 6-7 (DP drifted)
print(T,cuts)
for k in range(10):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',F,'-ss',str(cuts[k]),'-to',str(cuts[k+1]),'assets/vo/%02d.wav'%(k+1)],check=True)
    print('%02d'%(k+1),round(cuts[k+1]-cuts[k],2))
