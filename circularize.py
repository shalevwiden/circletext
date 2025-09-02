circulartext=' Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat Cat'
print(f'\nLenght of circular text is:\n{len(circulartext)}')

def circularize(text):
    spans=''
    for index,letter in enumerate(text):
        spantemplate=f'<span style="--i: {index}">{letter}</span>\n'
        spans+=spantemplate



    outputdiv=f'''
    <div class="circle-text">
        {spans}
    </div>
'''
    return outputdiv

print(circularize(circulartext))