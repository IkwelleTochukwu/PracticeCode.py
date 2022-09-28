#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
# py.exe mcb.pyw delete_all - delete all the keywords in the clipboard.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

# save and delete clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif  len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf.keys():
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list the keywords, load contents and delete all contents.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete_all':   # delete all contents in the clipboard
        mcbShelf.clear()

mcbShelf.close()

    



        



    
 