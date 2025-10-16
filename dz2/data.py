fh = open("cats_file.txt", 'w+', encoding="utf-8") 
lines = fh.writelines(['60b90c1c13067a15887e1ae1,Tayson,3\n', '60b90c2413067a15887e1ae2,Vika,1\n',
                  '60b90c2e13067a15887e1ae3,Barsik,2\n', '60b90c3b13067a15887e1ae4,Simon,12\n',
                  '60b90c4613067a15887e1ae5,Tessi,5'])

fh.close()