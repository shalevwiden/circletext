circulartext='Kris Kris Kris'
print(f'\nLenght of circular text is:\n{len(circulartext)}')

def makeoutputdiv(text,repeats):
    fulltext=text*int(repeats.strip())
    spans=''
    for index,letter in enumerate(fulltext):
        spantemplate=f'<span style="--i: {index*1}">{letter}</span>\n'
        spans+=spantemplate



    outputdiv=f'''
    <div class="circle-text">
        {spans}
    </div>
'''
    return outputdiv,len(fulltext)

