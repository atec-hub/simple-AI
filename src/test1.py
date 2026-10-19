from core import core

sentence11='ben seni cok seviyorum.'
sentence12='seni cok seviyorum.'

sentence21='bu benim icin cok zor.'
sentence22='bana cok zor.'

sentence31='bu benim kalemim.'
sentence32='benim kalemim.'
sentence33='bu benim.'

sentence41='benim adim ertan.'
sentence42='bu benim esim.'

soru11='nezaman geldi.'
soru12='nezaman geldiler.'
soru13='onlar nezaman geldi?'
soru14='onlar geldimi.'
soru15='onlarmi geldi.'
soru16='geldimi.'
soru17='geldilermi.'
soru18='kim geldi.'
soru19='kimler geldi.'

xxx10='bu birler kalem.'

core.think(xxx10)

print('1>',core.segment.scop1)
print('2>',core.segment.scop2)
print('3>',core.segment.scop3)
print('4>',core.segment.indk1)

print("-- end --")