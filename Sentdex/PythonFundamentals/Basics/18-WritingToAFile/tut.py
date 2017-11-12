
text = "Sample Test to Save \nNew Line!"

saveFile = open("exampleFile.txt", "w")
saveFile.write(text)
saveFile.close()

#'../../' to go 2 directories in front of the scripts file path
#Or we can specify the entire file path!

