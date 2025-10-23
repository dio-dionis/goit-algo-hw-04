def total_salary(path: str) -> tuple[float, float]:
    
        with open(path, "r", encoding="utf-8") as file:
            
            salaries = [
                float(line.split(',')[1])
                for line in file
                if line.strip() and len(line.split()) == 2
            ]
        
        if not salaries:
            return (0, 0)  # якщо файл порожній або дані некоректні
        
        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)
    
   

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")