import exifread

def main():
    path = raw_input('\nEnter path of Image file: ')
    print ''
    f = open(str(path), 'rb')
    tags = exifread.process_file(f)
    for tag in tags.keys():
        print str(tag)+': '+str(tags[tag])

if __name__ == '__main__':
    main()
