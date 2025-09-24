circulartext='Circle Text mf'
print(f'\nLenght of circular text is:\n{len(circulartext)}')

def makespans(maintext,repeats):
    fulltext=maintext*int(repeats.strip())
    spans=''
    for index,letter in enumerate(fulltext):
        spantemplate=f'<span style="--i: {index*1}">{letter}</span>\n'
        spans+=spantemplate



    spans=f'''
        {spans}
'''
    return spans

