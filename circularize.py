circulartext='Circle Text mf'
print(f'\nLenght of circular text is:\n{len(circulartext)}')

def makeoutputdiv(maintext,repeats):
    fulltext=maintext*int(repeats.strip())
    spans=''
    for index,letter in enumerate(fulltext):
        spantemplate=f'<span style="--i: {index*1}">{letter}</span>\n'
        spans+=spantemplate



    outputdiv=f'''
    <div class="circle-text" id="outputdiv1"> 
        {spans}
    </div>
'''
    return outputdiv

