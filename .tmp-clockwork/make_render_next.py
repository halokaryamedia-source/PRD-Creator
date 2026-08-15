#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

BULLET = re.compile(r'^(\s*)-\s+\*\*(.+?)\*\*(?::|\s+—\s+)?\s*(.*)$')
HEAD = re.compile(r'^(#{2,5})\s+(.+?)\s*$')

def clean_title(s:str)->str:
    return s.strip().rstrip(':').strip()

def slug(s:str)->str:
    s=s.lower().replace('’',"'")
    s=re.sub(r"[^a-z0-9]+","-",s).strip('-')
    return s

def section(lines, start, level, title=None):
    j=start+1
    while j < len(lines):
        m=HEAD.match(lines[j])
        if m and len(m.group(1)) <= level:
            break
        j+=1
    return lines[start+1:j], j

def headings(lines, level, start=0, end=None):
    end=len(lines) if end is None else end
    out=[]
    for i in range(start,end):
        m=HEAD.match(lines[i])
        if m and len(m.group(1))==level:
            out.append((i,m.group(2)))
    return out

def parse_named_bullets(block, indent=0):
    out=[]
    i=0
    while i < len(block):
        line=block[i]
        m=BULLET.match(line)
        if m and len(m.group(1)) == indent:
            title=clean_title(m.group(2)); desc=m.group(3).strip()
            if not desc and i+1 < len(block) and block[i+1].startswith('  - ') and not BULLET.match(block[i+1]):
                desc=block[i+1][4:].strip(); i+=1
            out.append({'title':title,'description':desc})
        i+=1
    return out

def split_subsections(block, level=4):
    out={}; current=None
    for line in block:
        m=HEAD.match(line)
        if m and len(m.group(1))==level:
            current=clean_title(m.group(2)); out[current]=[]
        elif current is not None:
            out[current].append(line)
    return out

def parse_requirements(block, level_design=False):
    groups=[]; g=None; item=None
    for line in block:
        hm=HEAD.match(line)
        if hm and len(hm.group(1))==5:
            g={'title':clean_title(hm.group(2)),'items':[]}; groups.append(g); item=None; continue
        m=BULLET.match(line)
        if m:
            indent=len(m.group(1)); title=clean_title(m.group(2)); rest=m.group(3).strip()
            if indent==0:
                if g is None:
                    g={'title':'Requirements','items':[]}; groups.append(g)
                if level_design:
                    area='—'
                    if rest.startswith('Area:'):
                        area=rest[5:].strip()
                    item={'object':title,'area_size':area,'build_and_visual':[],'gameplay_function':''}
                else:
                    item={'title':title,'details':[],'result':''}
                g['items'].append(item)
        if item is not None and line.startswith('  - '):
            t=line[4:].strip()
            if level_design:
                if t.startswith('Build/Visual:'): item['build_and_visual'].append(t.split(':',1)[1].strip())
                elif t.startswith('Gameplay Function:'): item['gameplay_function']=t.split(':',1)[1].strip()
            else:
                if t.startswith('Requirement:'): item['details'].append(t.split(':',1)[1].strip())
                elif t.startswith('Result:'): item['result']=t.split(':',1)[1].strip()
                elif t.startswith('Gameplay Function:'): item['result']=t.split(':',1)[1].strip()
    return groups

def parse_terms(block):
    out=[]
    for x in parse_named_bullets(block):
        out.append({'key':slug(x['title']), 'label':x['title'], 'definition':x['description']})
    return out

def parse_score(block):
    top=None; components=[]; meta={}
    for line in block:
        m=BULLET.match(line)
        if not m: continue
        indent=len(m.group(1)); title=clean_title(m.group(2)); desc=m.group(3).strip()
        if indent==0 and top is None:
            top=(title,desc); continue
        if indent>=2:
            cm=re.match(r'(.+?)\s*\((\d+%)\)$', title)
            if cm and '—' not in title:
                components.append({'name':cm.group(1).strip(),'weight':cm.group(2),'rule':desc}); continue
            key=title.lower().replace(' ','_').replace('-','_').replace('/','_')
            mapping={'timer_start':'timer_start','timer_stop':'timer_stop','no_score_condition':'no_score_condition','duplicate_prevention':'duplicate_prevention','final_result':'final_result_relationship','player_facing_result':'player_facing_display','telemetry___export':'telemetry_export','telemetry_export':'telemetry_export'}
            meta[mapping.get(key,key)]=desc
    if not top: return None
    name,desc=top
    parts=[p.strip() for p in desc.split('—')]
    d={'produces_score':True,'score_name':name,'scale':parts[0] if parts else '0–100','formula':parts[1] if len(parts)>1 else desc,'components':components}
    d.update(meta)
    return d

def parse_completion(block):
    top=None
    for line in block:
        m=BULLET.match(line)
        if m and len(m.group(1))==0:
            top=(clean_title(m.group(2)),m.group(3).strip()); break
    if not top: return None
    return {'produces_score':False,'completion_name':top[0],'handoff_result':'','summary':''}

def parse_reset(block):
    reset=[]; result=''
    for line in block:
        m=BULLET.match(line)
        if m and len(m.group(1))==0:
            title=clean_title(m.group(2)); desc=m.group(3).strip()
            if title=='Reset Result': result=desc
            else: reset.append((title + (' — '+desc if desc else '')).strip())
        elif line.startswith('- '):
            reset.append(line[2:].strip())
    return reset,result

def parse_package(lines, start, end, title):
    block=lines[start+1:end]
    label=''
    for l in block[:5]:
        if l.startswith('**') and l.endswith('**'): label=l.strip('*'); break
    subs=split_subsections(block,3)
    go=subs['Gameplay Overview']; gsub=split_subsections(go,4)
    vals={}
    for l in go:
        m=re.match(r'^\*\*(Context|Main Objective|Result):\*\*\s*(.*)$',l)
        if m: vals[m.group(1)]=m.group(2).strip()
    info={x['title']:x['description'] for x in parse_named_bullets(gsub['Gameplay Information'])}
    gameplay={'context':vals.get('Context',''),'main_objective':vals.get('Main Objective',''),'result':vals.get('Result',''),'purpose':info.get('Game Purpose',''),'gameplay_time':info.get('Gameplay Time',''),'start_condition':info.get('Starting Condition',''),'end_condition':info.get('End Condition',''),'blocked_or_fail_condition':info.get('Fail Condition',''),'scoring_criteria':info.get('Scoring Criteria',''),'player_flow':parse_named_bullets(gsub['Gameplay Flow'])}
    ld=subs['Level Design']; ldsub=split_subsections(ld,4)
    ld_over=next((l.strip() for l in ld if l.strip() and not HEAD.match(l)), '')
    level={'overview':ld_over,'flow':parse_named_bullets(ldsub['Design Flow']),'requirements':parse_requirements(ldsub['Build Requirements'],True),'notes':parse_named_bullets(ldsub['Important Build Notes'])}
    dev=subs['Developer']; dsub=split_subsections(dev,4)
    dev_over=next((l.strip() for l in dev if l.strip() and not HEAD.match(l)), '')
    developer={'overview':dev_over,'flow':parse_named_bullets(dsub['Development Flow']),'requirements':parse_requirements(dsub['Development Requirements']),'notes':parse_named_bullets(dsub['Important Development Notes'])}
    if 'Scoring Setup' in dsub: developer['scoring']=parse_score(dsub['Scoring Setup'])
    if 'Completion and Data' in dsub: developer['completion_data']=parse_completion(dsub['Completion and Data'])
    reset,result=parse_reset(dsub['Reset / Interruption']); developer['reset']=reset; developer['reset_result']=result
    return {'id':slug(title),'title':title,'package_label':label,'gameplay':gameplay,'level_design':level,'developer':developer,'terms':parse_terms(dsub.get('Terms',[])),'acceptance':[l[2:].strip() for l in dsub.get('Acceptance',[]) if l.startswith('- ')]}

def main(src,out):
    raw=src.read_bytes(); lines=raw.decode('utf-8').splitlines()
    title=lines[0][2:].strip(); meta={}
    for l in lines[:8]:
        m=re.match(r'^-\s+([^:]+):\s*(.+)$',l)
        if m: meta[m.group(1).strip()]=m.group(2).strip()
    data={'document':{'title':title,'brand':title,'brand_mark':'TC','document_type':meta.get('Document Type','Adventure Map'),'map_type':meta.get('Document Type','Adventure Map'),'subtitle':'Gameplay & Development Specification','version':meta.get('Version','1.0.0'),'languages':['en']}}
    h2=headings(lines,2); h2map={t:i for i,t in h2}
    oi=h2map['01. Overview']; oend=next(i for i,t in h2 if i>oi); ob=lines[oi+1:oend]
    project_context=next((l.strip() for l in ob if l.strip() and not HEAD.match(l) and not l.startswith('- ')), '')
    facts=[]
    for l in ob:
        m=re.match(r'^-\s+\*\*(.+?):\*\*\s*(.*)$',l)
        if m: facts.append({'key':slug(m.group(1)),'label':m.group(1),'value':m.group(2)})
    osubs=split_subsections(ob,3); journey=[]
    for l in osubs['Complete Gameplay Journey']:
        m=re.match(r'^\d+\.\s+\*\*(.+?)\*\*\s+—\s+(.*)$',l)
        if m: journey.append({'title':m.group(1),'description':m.group(2)})
    data['overview']={'project_context':project_context,'facts':facts,'journey':journey,'global_gameplay_direction':parse_named_bullets(osubs['Global Gameplay Direction'])}
    fi=h2map['02. Gameplay Flow']; fend=next(i for i,t in h2 if i>fi); flows=[]; hs=headings(lines,3,fi+1,fend)
    for k,(idx,t) in enumerate(hs):
        end=hs[k+1][0] if k+1<len(hs) else fend; b=lines[idx+1:end]
        narrative=next((l.strip() for l in b if l.strip() and not l.startswith('- ') and not HEAD.match(l)), '')
        beats=[]; nxt=''
        for x in parse_named_bullets(b):
            if x['title']=='Transition': nxt=x['description']
            else: beats.append(x)
        fid={'The Journey Begins':'journey-begins','The Vault Awakens':'vault-restored'}.get(t,slug(t))
        flows.append({'id':fid,'title':t,'display_title':t,'narrative_context':narrative,'beats':beats,'next_destination':nxt,'eyebrow':beats[0]['title'] if beats else t})
    data['gameplay_flow']=flows
    gi=h2map['03. Global Development']; gend=next(i for i,t in h2 if i>gi); gl=[]; ghs=headings(lines,3,gi+1,gend)
    gidmap={'Development Overview':'development-overview','Game System':'game-system','Data and Reset':'data-reset','Gameplay Development':'gameplay-development'}
    for k,(idx,t) in enumerate(ghs):
        end=ghs[k+1][0] if k+1<len(ghs) else gend; b=lines[idx+1:end]; sub=split_subsections(b,4)
        gl.append({'id':gidmap[t],'title':t,'subtitle':'Project-wide development','overview':next((l.strip() for l in b if l.strip() and not HEAD.match(l)), ''),'flow':parse_named_bullets(sub['Development Flow']),'requirements':parse_requirements(sub['Development Requirements']),'notes':parse_named_bullets(sub['Important Development Notes'])})
    data['global_development']=gl
    pkgs=[]; pheads=[(i,t) for i,t in h2 if re.match(r'0[4-9]\. ',t)]
    for k,(idx,ht) in enumerate(pheads):
        end=pheads[k+1][0] if k+1<len(pheads) else len(lines); _,pt=ht.split('. ',1); pkgs.append(parse_package(lines,idx,end,pt))
    data['packages']=pkgs; data['canonical_content_sha256']=hashlib.sha256(raw).hexdigest()
    out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':
    main(Path(sys.argv[1]),Path(sys.argv[2]))
