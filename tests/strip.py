
bodyString = "sjdklfjsdlfjslkdfjlsjdflkj\n sdkfhskdfjdskjhfkjshfkjhsk\n\n\nskfjdsjfslkdfjlskdjflsjdflkjldksfj\n\nhjgjhgjhgjhghj"

bodyString.split('\n')
bodyString = '\n'.join([line for line in bodyString.split('\n') if line.strip()])
print(bodyString)