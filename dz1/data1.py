fh = open("salary_file.txt", 'w+', encoding="utf-8")
data = fh.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\nYurii Petrov,4000\nOleg Sidorov,5000")
fh.close()