def sepit(contents):
    returndict = dict()
    for cont in contents:
        lower = cont.lower()
        if not lower.isalpha(): 
            continue
        elif lower in returndict:
            returndict[lower] += 1
        else:
            returndict[lower] = 0

    return dict(sorted(returndict.items(), key=lambda item: item[1], reverse=True))

#book report could be anything file related
bookreport = 'bookbot/books/frankenstein.txt'
with open(bookreport) as f:
    file_contents = f.read()
    word_count = len(file_contents.split());
    letters = sepit(file_contents)
    print(type(letters))
    print(f'--- Begin report of books {bookreport} ---')
    print(f'{word_count} words found in the document')
    for k, v in letters.items():
        print(f"The '{k}' characters was found {v} times")
    print('--- End of Report ---')