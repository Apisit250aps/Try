from collections import deque
# Independent bounded fixture: B is behavior rather than a displayed option.
transitions = {
 'start': [('A','join',lambda s: True, lambda s: 1),('B','join',lambda s: True,lambda s: 2)],
 'join': [('recall','resolve',lambda s: s in (1,2),lambda s:s)],
 'resolve': [('E1','e1',lambda s:s==1,lambda s:s),('E2','e2',lambda s:s==2,lambda s:s)],
}
seen={('start',0)}; q=deque([('start',0)]); trace={('start',0):[]}
while q:
 n,s=q.popleft()
 for label,dst,guard,effect in transitions.get(n,[]):
  if guard(s):
   target=(dst,effect(s))
   if target not in seen: seen.add(target); trace[target]=trace[n,s]+[label]; q.append(target)
assert trace['e1',1]==['A','recall','E1'] and trace['e2',2]==['B','recall','E2']
assert not any(n=='e3' for n,s in seen)
assert all(transitions.get(n) or n in {'e1','e2'} for n,s in seen)
assert [name for name,p in [('E1',lambda s:s==1),('E4',lambda s:s>0)] if p(1)]==['E1','E4']
assert not any(p(0) for p in [lambda s:s==1,lambda s:s==2])
assert len({s for n,s in seen if n=='join'})==2
# Intentional hub can exit yet admits an infinite self-loop; closed cycle cannot exit.
graph={'hub':['hub','end'],'closed':['closed']}
assert 'end' in graph['hub'] and graph['closed']==['closed']
print('PASS finite fixture: 7 node-state pairs; 2 ending witnesses; preserved join state')
print('PASS overlapping guards witness state=1; uncovered guard witness state=0')
print('PASS unreachable e3; cycle examples classified by explicit edge inspection')
print('LIMIT: hand-authored fixture; no generic validator, narrative model or runtime exercised')
