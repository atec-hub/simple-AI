from core import core

sentences={
    11 : 'ben seni cok seviyorum.',
    12 : 'seni cok seviyorum.',

    21 : 'bu benim icin cok zor.',
    22 : 'bana cok zor.',

    31 : 'bu benim kalemim.',
    32 : 'benim kalemim.',
    33 : 'bu benim.',

    41 : 'benim adim ertan.',
    42 : 'bu benim esim.',

    51 : 'nezaman geldi.',
    52 : 'nezaman geldiler.',
    53 : 'onlar nezaman geldi.',
    54 : 'onlar geldimi.',
    55 : 'onlarmi geldi.',
    56 : 'geldimi.',
    57 : 'geldilermi.',
    58 : 'kim geldi.',
    59 : 'kimler geldi.',
    
    60 : 'onlar bugUn geldi.',
    61 : 'onlar bugUn geldiler.',
    62 : 'orada havalar nasIl.', # ????
}

keys=sorted(sentences)
for no in keys:
    sentence=sentences[no]
    core.clr()
    core.think(sentence)
    print("%2d:" % no,core.segment.scop1,core.segment.scop2,core.segment.scop3,core.segment.indk1)

print("-- end --")